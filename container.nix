{ pkgs, ytgo-bot, ... }:
pkgs.dockerTools.buildImage {
  name = "ytgo-bot";
  tag = "1.1.2";
  copyToRoot = pkgs.buildEnv {
    name = "image-root";
    paths = [ ytgo-bot ];
    pathsToLink = [ "/bin" ];
  };
  config = {
    Cmd = [ "bot.py" ];
    ExposedPorts = {
      "10000" = { };
    };
  };
}
