function run_cmd(){
	cmd=$1
	check_res=$2
	$cmd
	if [ $? -ne 0 ]; then
		echo "$cmd failed"
		if [ x$check_res != x0 ]; then
			exit 1
		fi
	fi
}

if [ $# != 4 ]; then
	echo "USAGE: sh $0 {user} {uid} {gid} {workdir} {command}"
	echo "   eg: sh $0 gpu_platform 1000 1000 /yiplatform_develop/work_dir \"pwd\""
fi

user=$1
uid=$2
gid=$3
workdir=$4
execcmd=$5
usernum=`cat /etc/passwd|grep -c "^${user}:.*:${uid}:${gid}"`
if [ x$usernum ==  x0 ]; then
	run_cmd "useradd -d -g ${gid} -u ${uid} -m ${username}"
fi
run_cmd "cd ${workdir}"
su - ${username} -s/bin/bash -c "${execcmd}"
