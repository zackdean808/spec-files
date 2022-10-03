Name:           discord
Version:        0.0.20
Release:        1%{?dist}
Summary:        This is a community supported spec file for packaging discord as an rpm. 

License:        GPL-2.0
URL:            https://discord.com/download
Source0:        discord-0.0.20.tar.gz



%description 
This is a spec file that can be used to create a discord rpm. 

%prep 
%setup -n Discord

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/opt/Discord/
install -d $RPM_BUILD_ROOT/%{_datarootdir}/applications/
install -d $RPM_BUILD_ROOT/opt/Discord/locales/
install -d $RPM_BUILD_ROOT/opt/Discord/resources/
install -d $RPM_BUILD_ROOT/opt/Discord/swiftshader/


install %{_builddir}/Discord/chrome_100_percent.pak $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/chrome_200_percent.pak $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/chrome-sandbox $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/Discord $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/discord.desktop $RPM_BUILD_ROOT/%{_datarootdir}/applications/
install %{_builddir}/Discord/discord.png $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/icudtl.dat $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/libEGL.so $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/libffmpeg.so $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/libGLESv2.so $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/libvk_swiftshader.so $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/postinst.sh $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/resources.pak $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/snapshot_blob.bin $RPM_BUILD_ROOT/opt/Discord/
install %{_builddir}/Discord/v8_context_snapshot.bin $RPM_BUILD_ROOT/opt/Discord/
install -d %{_builddir}/Discord/locales/ $RPM_BUILD_ROOT/opt/Discord/
install -d %{_builddir}/Discord/resources/ $RPM_BUILD_ROOT/opt/Discord/
install -d %{_builddir}/Discord/swiftshader/ $RPM_BUILD_ROOT/opt/Discord/


%files
%attr(0744, root, root)
/opt/Discord/chrome_100_percent.pak
/opt/Discord/chrome_200_percent.pak
/opt/Discord/chrome-sandbox
/opt/Discord/Discord
%{_datarootdir}/applications/discord.desktop
/opt/Discord/discord.png
/opt/Discord/icudtl.dat
/opt/Discord/libEGL.so
/opt/Discord/libffmpeg.so
/opt/Discord/libGLESv2.so
/opt/Discord/libvk_swiftshader.so
/opt/Discord/locales/
/opt/Discord/postinst.sh
/opt/Discord/resources/
/opt/Discord/resources.pak
/opt/Discord/snapshot_blob.bin
/opt/Discord/swiftshader/
/opt/Discord/v8_context_snapshot.bin


%changelog
* Sun Oct 02 2022 Zack D. <zack.dean@gmail.com>
- New version 
- Moved evertying to /opt 

* Sun Dec 05 2021 Zack D. <zack.dean@gmail.com>
- initial build 
