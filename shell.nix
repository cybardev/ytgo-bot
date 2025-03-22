{
  pkgs ? import <nixpkgs> {
    config = { };
    overlays = [ ];
  },
}:
pkgs.mkShellNoCC {
  packages = with pkgs; [
    python312
    python312Packages.discordpy
  ];
  # shellHook = "python main.py";
}
