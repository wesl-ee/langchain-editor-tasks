let
  nixpkgs = import <nixpkgs> { };
in
with nixpkgs;
stdenv.mkDerivation {
  name = "llm-playground";
  buildInputs = [
    python311
    python311Packages.pip
  ];
  LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
}
