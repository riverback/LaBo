steps = 8
n_runs = 1
img_path = 'datasets/CUB/images/'
data_root = 'exp/linear_probe/CUB'
img_split_path = 'datasets/CUB/splits'
num_cls = 200
unfreeze_clip = False
paper = True
cls_names = [
    'black footed albatross', 'laysan albatross', 'sooty albatross',
    'groove billed ani', 'crested auklet', 'least auklet', 'parakeet auklet',
    'rhinoceros auklet', 'brewer blackbird', 'red winged blackbird',
    'rusty blackbird', 'yellow headed blackbird', 'bobolink', 'indigo bunting',
    'lazuli bunting', 'painted bunting', 'cardinal', 'spotted catbird',
    'gray catbird', 'yellow breasted chat', 'eastern towhee',
    'chuck will widow', 'brandt cormorant', 'red faced cormorant',
    'pelagic cormorant', 'bronzed cowbird', 'shiny cowbird', 'brown creeper',
    'american crow', 'fish crow', 'black billed cuckoo', 'mangrove cuckoo',
    'yellow billed cuckoo', 'gray crowned rosy finch', 'purple finch',
    'northern flicker', 'acadian flycatcher', 'great crested flycatcher',
    'least flycatcher', 'olive sided flycatcher', 'scissor tailed flycatcher',
    'vermilion flycatcher', 'yellow bellied flycatcher', 'frigatebird',
    'northern fulmar', 'gadwall', 'american goldfinch', 'european goldfinch',
    'boat tailed grackle', 'eared grebe', 'horned grebe', 'pied billed grebe',
    'western grebe', 'blue grosbeak', 'evening grosbeak', 'pine grosbeak',
    'rose breasted grosbeak', 'pigeon guillemot', 'california gull',
    'glaucous winged gull', 'heermann gull', 'herring gull', 'ivory gull',
    'ring billed gull', 'slaty backed gull', 'western gull',
    'anna hummingbird', 'ruby throated hummingbird', 'rufous hummingbird',
    'green violetear', 'long tailed jaeger', 'pomarine jaeger', 'blue jay',
    'florida jay', 'green jay', 'dark eyed junco', 'tropical kingbird',
    'gray kingbird', 'belted kingfisher', 'green kingfisher',
    'pied kingfisher', 'ringed kingfisher', 'white breasted kingfisher',
    'red legged kittiwake', 'horned lark', 'pacific loon', 'mallard',
    'western meadowlark', 'hooded merganser', 'red breasted merganser',
    'mockingbird', 'nighthawk', 'clark nutcracker', 'white breasted nuthatch',
    'baltimore oriole', 'hooded oriole', 'orchard oriole', 'scott oriole',
    'ovenbird', 'brown pelican', 'white pelican', 'western wood pewee',
    'sayornis', 'american pipit', 'whip poor will', 'horned puffin',
    'common raven', 'white necked raven', 'american redstart', 'geococcyx',
    'loggerhead shrike', 'great grey shrike', 'baird sparrow',
    'black throated sparrow', 'brewer sparrow', 'chipping sparrow',
    'clay colored sparrow', 'house sparrow', 'field sparrow', 'fox sparrow',
    'grasshopper sparrow', 'harris sparrow', 'henslow sparrow',
    'le conte sparrow', 'lincoln sparrow', 'nelson sharp tailed sparrow',
    'savannah sparrow', 'seaside sparrow', 'song sparrow', 'tree sparrow',
    'vesper sparrow', 'white crowned sparrow', 'white throated sparrow',
    'cape glossy starling', 'bank swallow', 'barn swallow', 'cliff swallow',
    'tree swallow', 'scarlet tanager', 'summer tanager', 'artic tern',
    'black tern', 'caspian tern', 'common tern', 'elegant tern',
    'forsters tern', 'least tern', 'green tailed towhee', 'brown thrasher',
    'sage thrasher', 'black capped vireo', 'blue headed vireo',
    'philadelphia vireo', 'red eyed vireo', 'warbling vireo',
    'white eyed vireo', 'yellow throated vireo', 'bay breasted warbler',
    'black and white warbler', 'black throated blue warbler',
    'blue winged warbler', 'canada warbler', 'cape may warbler',
    'cerulean warbler', 'chestnut sided warbler', 'golden winged warbler',
    'hooded warbler', 'kentucky warbler', 'magnolia warbler',
    'mourning warbler', 'myrtle warbler', 'nashville warbler',
    'orange crowned warbler', 'palm warbler', 'pine warbler',
    'prairie warbler', 'prothonotary warbler', 'swainson warbler',
    'tennessee warbler', 'wilson warbler', 'worm eating warbler',
    'yellow warbler', 'northern waterthrush', 'louisiana waterthrush',
    'bohemian waxwing', 'cedar waxwing', 'american three toed woodpecker',
    'pileated woodpecker', 'red bellied woodpecker', 'red cockaded woodpecker',
    'red headed woodpecker', 'downy woodpecker', 'bewick wren', 'cactus wren',
    'carolina wren', 'house wren', 'marsh wren', 'rock wren', 'winter wren',
    'common yellowthroat'
]
img_ext = ''
clip_model = 'ViT-L/14'
lr = 0.001
bs = 128
n_shots = 8
dataset = 'CUB'
