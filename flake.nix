{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixos-25.05";
    cypkgs = {
      url = "github:cybardev/nix-channel?ref=main";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
  outputs =
    { nixpkgs, ... }@inputs:
    let
      forEachSystem =
        f:
        nixpkgs.lib.genAttrs nixpkgs.lib.systems.flakeExposed (
          system:
          f {
            pkgs = import nixpkgs {
              inherit system;
              overlays = [ inputs.cypkgs.overlays.default ];
            };
          }
        );
    in
    {
      devShells = forEachSystem (
        { pkgs }:
        {
          default = import ./shell.nix { inherit pkgs; };
        }
      );

      packages = forEachSystem (
        { pkgs }:
        let
          ytgo-bot = import ./package.nix { inherit pkgs; };
        in
        {
          inherit ytgo-bot;
          default = ytgo-bot;
          image = import ./container.nix { inherit pkgs ytgo-bot; };
        }
      );
    };
}
