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
      src = pkgs.fetchFromGitHub {
        owner = "Pycord-Development";
        repo = "pycord";
        tag = "v${version}";
        hash = "sha256-35GfgXmTED3/jmshRwtRXPns+UkeKX2tG1ksGTfwjnY=";
      };
    };
in
python.pkgs.buildPythonApplication {
  pname = "ytgo-bot";
  version = "0.1.0";
  propagatedBuildInputs = with pythonPackages; [
    pycord
    aiohttp
    faust-cchardet
    msgspec
    yarl
    (pkgs.cy.ytgo.overrideAttrs (
      finalAttrs: previousAttrs: {
        postFixup = "";
      }
    ))
  ];
  src = ./.;
  meta.mainProgram = "ytgo-bot.py";
}
