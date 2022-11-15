{
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-unstable;
  };
  outputs = {self, nixpkgs, ...}@inputs: let
    supportedSystems = [ "x86_64-linux" ];
    pkgs = nixpkgs.legacyPackages;
    perSystem = nixpkgs.lib.genAttrs supportedSystems;
  in {
    devShells = perSystem (system: {
      default = pkgs.${system}.mkShell {
        packages = with pkgs.${system}; [
          (python39.withPackages (p: with p; [
            jinja2
            htmlmin
            pillow
          ]))
        ];
      };
    });
  };
}
