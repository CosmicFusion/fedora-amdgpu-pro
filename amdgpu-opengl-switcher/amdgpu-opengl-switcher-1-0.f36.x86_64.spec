Name:          amdgpu-opengl-switcher
Version:       1
Release:       0%{?dist}
License:       GPL
Group:         Unspecified
Summary:       Select needed OpenGL implementation with gl_mesa, gl_zink or gl_pro prefix


URL:           https://github.com/Ashark/archlinux-amdgpu-pro/blob/master/progl






Provides:      amdgpu-opengl-switcher = 1-0.fc36
Provides:      amdgpu-opengl-switcher(x86-64) = 1-0.fc36
Requires:      /usr/bin/bash

%install
tar -xf amdgpu-opengl-switcher-1-0.f36.x86_64.tar.gz
mv usr %{buildroot}/

%description
Select needed opengl implementation with gl_mesa, gl_zink or gl_pro prefix
%files
%attr(0755, root, root) "/usr/bin/gl_zink"
%attr(0755, root, root) "/usr/bin/gl_pro"
%attr(0755, root, root) "/usr/bin/gl_mesa"
%attr(0644, root, root) "/usr/share/bash-completion/completions/gl_zink"
%attr(0644, root, root) "/usr/share/bash-completion/completions/gl_pro"
%attr(0644, root, root) "/usr/share/bash-completion/completions/gl_mesa"

