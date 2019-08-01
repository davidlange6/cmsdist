#!/bin/bash
dir=$(dirname $0)
if [ -e "${dir}/$1.spec" ] ; then
  cat "${dir}/$1.spec"
else
  echo "### RPM external $1 $2"
  if [ "$4" == "py2" ] ; then
    echo "%define doPython3 no"
  fi
  if [ "$4" == "py3" ] ; then
    echo "%define doPython2 no"
  fi

  echo "## IMPORT build-with-pip"
  if [ -f "${dir}/$1.file" ] ; then
    subdir=$(basename $dir)
    echo ""
    echo "## INCLUDE ${subdir}/${1}"
  fi
fi
