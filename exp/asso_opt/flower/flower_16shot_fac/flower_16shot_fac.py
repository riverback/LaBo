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
submodular_weights = [10000000.0, 1]
proj_name = 'flower'
concept_root = 'datasets/flower/concepts/'
img_split_path = 'datasets/flower/splits'
img_path = 'datasets/flower/images'
concept_type = 'all_submodular'
img_ext = '.jpg'
raw_sen_path = 'datasets/flower/concepts/concepts_raw.npy'
concept2cls_path = 'datasets/flower/concepts/concept2cls.npy'
cls_name_path = 'datasets/flower/concepts/cls_names.npy'
num_cls = 102
bs = 256
on_gpu = True
num_concept = 2550
lr = 1e-05
max_epochs = 10000
n_shots = 16
data_root = 'exp/asso_opt/flower/flower_16shot_fac'
