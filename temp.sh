#CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh HAM10000 1 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh HAM10000 2 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh HAM10000 4 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh HAM10000 8 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh HAM10000 16 ViT-L/14
CUDA_VISIBLE_DEVICES=0 sh linear_probe.sh HAM10000 all ViT-L/14

# CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 1 HAM10000
# CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 2 HAM10000
# CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 4 HAM10000
# CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 8 HAM10000
# CUDA_VISIBLE_DEVICES=0 bash labo_train.sh 16 HAM10000
# CUDA_VISIBLE_DEVICES=0 bash labo_train.sh all HAM10000
