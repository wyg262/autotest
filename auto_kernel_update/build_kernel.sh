#!/bin/sh

sh -c 'yes "" | make oldconfig'
sleep 10

make bzImage

if [ $? != 0 ];then
	echo "make bzImage failed!" && exit 2
else
	:
fi	

sleep 10

make modules

if [ $? != 0 ];then
        echo "make modules failed!" && exit 2
else
        :
fi

sleep 10

make modules_install

if [ $? != 0 ];then
        echo "make modules_intall failed!" && exit 2
else
        :
fi

sleep 10

make install

if [ $? != 0 ];then
        echo "make install failed!" && exit 2
else
        :
fi

echo "kernel make successful!"




