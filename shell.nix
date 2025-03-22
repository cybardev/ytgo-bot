{
  pkgs ? import <nixpkgs> {
    config = { };
    overlays = [ ];
  },
  ...
}:
let
  pythonPackages = pkgs.python313Packages;
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
pkgs.mkShell {
  packages = with pythonPackages; [
    python
    pip
    pycord
  ];
}
