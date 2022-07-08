Name:           discord
Version:        0.0.18
Release:        1%{?dist}
Summary:        This is a community supported spec file for packaging discord as an rpm. 

License:        GPL-2.0
URL:            https://discord.com/download
Source0:        discord-0.0.18.tar.gz



%description 
This is a spec file that can be used to create a discord rpm. 

%prep 
%setup -n Discord

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install -d $RPM_BUILD_ROOT/%{_datarootdir}/applications/
install -d $RPM_BUILD_ROOT/%{_datarootdir}/Discord/locales/
install -d $RPM_BUILD_ROOT/%{_datarootdir}/Discord/resources/
install -d $RPM_BUILD_ROOT/%{_datarootdir}/Discord/swiftshader/


install %{_builddir}/Discord/chrome_100_percent.pak $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/chrome_200_percent.pak $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/chrome-sandbox $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/Discord $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/discord.desktop $RPM_BUILD_ROOT/%{_datarootdir}/applications/
install %{_builddir}/Discord/discord.png $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/icudtl.dat $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/libEGL.so $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/libffmpeg.so $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/libGLESv2.so $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/libvk_swiftshader.so $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/postinst.sh $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/resources.pak $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/snapshot_blob.bin $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install %{_builddir}/Discord/v8_context_snapshot.bin $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install -d %{_builddir}/Discord/locales/ $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install -d %{_builddir}/Discord/resources/ $RPM_BUILD_ROOT/%{_datarootdir}/Discord/
install -d %{_builddir}/Discord/swiftshader/ $RPM_BUILD_ROOT/%{_datarootdir}/Discord/


%files
%attr(0744, root, root)
%{_datarootdir}/Discord/chrome_100_percent.pak
%{_datarootdir}/Discord/chrome_200_percent.pak
%{_datarootdir}/Discord/chrome-sandbox
%{_datarootdir}/Discord/Discord
%{_datarootdir}/applications/discord.desktop
%{_datarootdir}/Discord/discord.png
%{_datarootdir}/Discord/icudtl.dat
%{_datarootdir}/Discord/libEGL.so
%{_datarootdir}/Discord/libffmpeg.so
%{_datarootdir}/Discord/libGLESv2.so
%{_datarootdir}/Discord/libvk_swiftshader.so
%{_datarootdir}/Discord/locales/
%{_datarootdir}/Discord/postinst.sh
%{_datarootdir}/Discord/resources/
%{_datarootdir}/Discord/resources.pak
%{_datarootdir}/Discord/snapshot_blob.bin
%{_datarootdir}/Discord/swiftshader/
%{_datarootdir}/Discord/v8_context_snapshot.bin


%changelog
* Sun Dec 05 2021 Zack D. <zack.dean@gmail.com>
- initial build 
