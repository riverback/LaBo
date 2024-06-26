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
submodular_weights = [10000000.0, 5]
proj_name = 'CIFAR10'
concept_root = 'datasets/CIFAR10/concepts/'
img_split_path = 'datasets/CIFAR10/splits'
img_path = 'datasets/CIFAR10/images'
concept_type = 'all_submodular'
img_ext = ''
raw_sen_path = 'datasets/CIFAR10/concepts/concepts_raw.npy'
concept2cls_path = 'datasets/CIFAR10/concepts/concept2cls.npy'
cls_name_path = 'datasets/CIFAR10/concepts/cls_names.npy'
num_cls = 10
bs = 512
on_gpu = True
num_concept = 500
lr = 0.0001
max_epochs = 15000
n_shots = 'all'
data_root = 'exp/asso_opt/CIFAR10/CIFAR10_allshot_fac'
