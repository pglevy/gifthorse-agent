{pkgs}: {
  deps = [
    pkgs.nodePackages.prettier
    pkgs.openssl
    pkgs.postgresql
  ];
}
