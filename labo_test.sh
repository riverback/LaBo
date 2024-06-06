# $1: cfg path
# $2: ckpt path
# bash labo_test.sh config_path ckpt_path
python main.py --cfg $1 --func asso_opt_main --test --cfg-options bs=512 ckpt_path=$2 ${@:3}