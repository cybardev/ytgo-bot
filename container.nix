{pkgs, ytgo-bot,...}:
pkgs.dockerTools.buildImage{
  name = "ytgo-bot";
  tag = "1.1.2";
  config = {
    WorkingDir = "/app";
    Cmd = [ (pkgs.lib.getExe ytgo-bot) ];
  };
}
