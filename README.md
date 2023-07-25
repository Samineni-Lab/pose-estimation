# Pose Estimation

This fork of [DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) aims to combine DeepLabCut and 
[Anipose](https://github.com/lambdaloop/anipose) into a cohesive GUI (expanding on DLC's original GUI). There may be a 
few other changes for personal preference (such as multi-GPU training), but no specific changes are planned. 

Additionally, this fork uses a modified version of [napari-deeplabcut](https://github.com/DeepLabCut/napari-deeplabcut),
primarily to include a method for viewing the in-video context of the frame a user is labeling. This stems from some
frames being confusing to label without knowing what happened before or after, such as an animal in a strange position
or in swift motion.