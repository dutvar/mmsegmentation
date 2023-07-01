
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class HubmapDataset(BaseSegDataset):

    METAINFO = dict(
        classes=('blood vessels'),
        palette=[])



    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='_label.png',
                 reduce_zero_label=False,
                 **kwargs) -> None:

        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)