# Instructions 
1. Create your rpm build tree ```rpmdev-setuptree```shell 
2. Move the tar.gz and .patch file ~/rpmbuild/SOURCES
3. Move spec file to ~/rpmbuild/SPECS
4. Build the package with ```rpmbuild -ba ~/rpmbuild/SPECS/discord.spec```shell 
5. Install the package ```rpm -ivh ~/rpmbuild/RPMS/x86_64/discord-$version.rpm```shell 
6. Profit 

## Download 
https://discord.com/download
