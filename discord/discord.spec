Name:           discord
Version:        0.0.16
Release:        1%{?dist}
Summary:        This is a community supported spec file for packaging discord as an rpm. 

License:        GPL-2.0
URL:            https://discord.com/download
Source0:        discord-0.0.16.tar.gz



%description This is a spec file that can be used to create a discord rpm. 


%setup -n Discord

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/share/Discord/
install -d $RPM_BUILD_ROOT/usr/share/applications/
install -d $RPM_BUILD_ROOT/usr/share/Discord/locales/
install -d $RPM_BUILD_ROOT/usr/share/Discord/resources/
install -d $RPM_BUILD_ROOT/usr/share/Discord/swiftshader/


install Discord/chrome_100_percent.pak $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/chrome_200_percent.pak $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/chrome-sandbox $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/Discord $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/discord.desktop $RPM_BUILD_ROOT/usr/share/applications/
install Discord/discord.png $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/icudtl.dat $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/libEGL.so $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/libffmpeg.so $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/libGLESv2.so $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/libvk_swiftshader.so $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/postinst.sh $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/resources.pak $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/snapshot_blob.bin $RPM_BUILD_ROOT/usr/share/Discord/
install Discord/v8_context_snapshot.bin $RPM_BUILD_ROOT/usr/share/Discord/
install -d Discord/locales/ $RPM_BUILD_ROOT/usr/share/Discord/
install -d Discord/resources/ $RPM_BUILD_ROOT/usr/share/Discord/
install -d Discord/swiftshader/ $RPM_BUILD_ROOT/usr/share/Discord/


%files
%attr(0744, root, root)
/usr/share/Discord/chrome_100_percent.pak
/usr/share/Discord/chrome_200_percent.pak
/usr/share/Discord/chrome-sandbox
/usr/share/Discord/Discord
/usr/share/applications/discord.desktop
/usr/share/Discord/discord.png
/usr/share/Discord/icudtl.dat
/usr/share/Discord/libEGL.so
/usr/share/Discord/libffmpeg.so
/usr/share/Discord/libGLESv2.so
/usr/share/Discord/libvk_swiftshader.so
/usr/share/Discord/locales/
/usr/share/Discord/postinst.sh
/usr/share/Discord/resources/
/usr/share/Discord/resources.pak
/usr/share/Discord/snapshot_blob.bin
/usr/share/Discord/swiftshader/
/usr/share/Discord/v8_context_snapshot.bin


%changelog
* Sun Dec 05 2021 Zack D. <zack.dean@gmail.com>
- initial build 
