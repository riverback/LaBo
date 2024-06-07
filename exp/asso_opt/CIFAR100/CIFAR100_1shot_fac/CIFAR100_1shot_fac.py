use_mi = True
group_select = True
clip_model = 'ViT-L/14'
use_rand_init = False
init_val = 1.0
asso_act = 'softmax'
use_l1_loss = False
use_div_loss = False
lambda_l1 = 0.01
lambda_div = 0.005
use_img_norm = False
use_txt_norm = False
cls_name_init = 'none'
cls_sim_prior = 'none'
remove_cls_name = False
concept_select_fn = 'submodular'
submodular_weights = [10000000.0, 7.5]
proj_name = 'CIFAR100'
concept_root = 'datasets/CIFAR100/concepts/'
img_split_path = 'datasets/CIFAR100/splits'
img_path = 'datasets/CIFAR100/images'
concept_type = 'all_submodular'
img_ext = ''
raw_sen_path = 'datasets/CIFAR100/concepts/concepts_raw.npy'
concept2cls_path = 'datasets/CIFAR100/concepts/concept2cls.npy'
cls_name_path = 'datasets/CIFAR100/concepts/cls_names.npy'
num_cls = 100
bs = 16
on_gpu = True
num_concept = 5000
lr = 1e-05
max_epochs = 10000
n_shots = 1
data_root = 'exp/asso_opt/CIFAR100/CIFAR100_1shot_fac'
