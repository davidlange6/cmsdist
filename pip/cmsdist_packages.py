def packages(virtual_packages):
  from os.path import dirname,join, exists
  pkg_dir = dirname(__file__)
  req = join(pkg_dir,'requirements.txt')
  if not exists(req): return
  for line in [ l.replace(' ','') for l in open(req).readlines()]:
    if line.startswith('#'):continue
    if not '==' in line: continue
    (pkg, ver) = line.strip().split('==',1)
    verSP=ver.split(',')
    ver2=verSP[0]
    if len(verSP)>1:
      ver3=verSP[1]
    else:
      ver3=ver2
    if ver2 != 'None':
      virtual_packages['py2-'+pkg]='%s/package.sh "py2-%s" "%s" "%s"' % (pkg_dir, pkg, ver2, 'py2')
    if ver3 != 'None':
      virtual_packages['py3-'+pkg]='%s/package.sh "py3-%s" "%s" "%s"' % (pkg_dir, pkg, ver3, 'py3')
  return
