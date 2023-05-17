import splitfolders

path = "C:/Users/janek/__haemorrhage_project__/__datasets__/x_lrg_formatted/all"
print("Splitting folder {} intro train/test folders".format(path))
splitfolders.ratio(path, output="output",
                  seed=1337, ratio=(.8, .2), group_prefix=None, move=False)