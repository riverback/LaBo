CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh food 1 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh food 2 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh food 4 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh food 8 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh food 16 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh food all ViT-L/14

CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 1 food
CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 2 food
CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 4 food
CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 8 food
CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 16 food
CUDA_VISIBLE_DEVICES=0 bash labo_train.sh all food