Name:           discord
Version:        0.0.26
Release:        1%{?dist}
Summary:        This is a community supported spec file for packaging discord as an rpm. 

License:        GPL-2.0
URL:            https://discord.com/download
Source0:        discord-0.0.25.tar.gz
Patch0:		desktop.patch


%description 
This is a spec file that can be used to create a discord rpm. 

%prep 
%setup -n Discord
%patch0 -p1 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install -d $RPM_BUILD_ROOT/%{_datarootdir}/applications/
install -d $RPM_BUILD_ROOT/%{_datarootdir}/discord/locales/
install -d $RPM_BUILD_ROOT/%{_datarootdir}/discord/resources/
install -d $RPM_BUILD_ROOT/%{_datarootdir}/discord/swiftshader/


install %{_builddir}/Discord/chrome_100_percent.pak $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/chrome_200_percent.pak $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/chrome-sandbox $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/Discord $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/discord.desktop $RPM_BUILD_ROOT/%{_datarootdir}/applications/
install %{_builddir}/Discord/discord.png $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/icudtl.dat $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/libEGL.so $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/libffmpeg.so $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/libGLESv2.so $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/libvk_swiftshader.so $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/postinst.sh $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/resources.pak $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/snapshot_blob.bin $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install %{_builddir}/Discord/v8_context_snapshot.bin $RPM_BUILD_ROOT/%{_datarootdir}/discord/
install -d %{_builddir}/Discord/locales $RPM_BUILD_ROOT/%{_datarootdir}/discord/
cp -a  %{_builddir}/Discord/swiftshader $RPM_BUILD_ROOT/%{_datarootdir}/discord/
cp -a  %{_builddir}/Discord/resources $RPM_BUILD_ROOT/%{_datarootdir}/discord/

%files
%attr(0744, root, root)
%{_datarootdir}/discord/chrome_100_percent.pak
%{_datarootdir}/discord/chrome_200_percent.pak
%{_datarootdir}/discord/chrome-sandbox
%{_datarootdir}/discord/Discord
%{_datarootdir}/applications/discord.desktop
%{_datarootdir}/discord/discord.png
%{_datarootdir}/discord/icudtl.dat
%{_datarootdir}/discord/libEGL.so
%{_datarootdir}/discord/libffmpeg.so
%{_datarootdir}/discord/libGLESv2.so
%{_datarootdir}/discord/libvk_swiftshader.so
%{_datarootdir}/discord/locales/
%{_datarootdir}/discord/postinst.sh
%{_datarootdir}/discord/resources
%{_datarootdir}/discord/resources.pak
%{_datarootdir}/discord/snapshot_blob.bin
%{_datarootdir}/discord/v8_context_snapshot.bin
%{_datarootdir}/discord/swiftshader/libEGL.so
%{_datarootdir}/discord/swiftshader/libGLESv2.so
%{_datarootdir}/discord/resources/app.asar
%{_datarootdir}/discord/resources/bootstrap/manifest.json
%{_datarootdir}/discord/resources/build_info.json

%changelog
* Sun Apr 16 2023 Zack D.<zack.dean@gmail.com>
  - New version 0.0.26

* Mon Mar 13 2023 Zack D. <zack.dean@gmail.com> 
  - Added patch0 to fix path in the /usr/share/applications directory 
  - updated build verison 

* Mon Mar 13 2023 Zack D. <zack.dean@gmail.com> 
  - New Version -> 0.25
  - bug fix of cp -r to cp -a 
* Sun Oct 02 2022 Zack D. <zack.dean@gmail.com>
  - New version 
  - Moved evertying to /%{_datarootdir} 

* Sun Dec 05 2021 Zack D. <zack.dean@gmail.com>
  - initial build 
