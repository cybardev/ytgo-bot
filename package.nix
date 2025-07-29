{ pkgs, ... }:
let
  python = pkgs.python312;
  pythonPackages = pkgs.python312Packages;
  pycord =
    let
      pname = "py_cord";
      version = "2.6.1";
    in
    pythonPackages.buildPythonPackage {
      doCheck = false;
      inherit pname version;
      src = pkgs.fetchPypi {
        inherit pname version;
        sha256 = "sha256-NgZPIl8se73f5ULV7VgfKldE9hjgOQk8980mWaWLx5s=";
      };
    };
in
python.pkgs.buildPythonApplication {
  pname = "ytgo-bot";
  version = "0.1.0";
  propagatedBuildInputs = with pythonPackages; [
    python
    pip
    pycord
    aiohttp
    faust-cchardet
    msgspec
    yarl
    pkgs.cy.ytgo
  ];
  src = ./.;
  meta.mainProgram = "bot.py";
}
