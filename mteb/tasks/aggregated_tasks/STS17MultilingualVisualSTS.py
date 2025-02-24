from __future__ import annotations

from mteb.abstasks import AbsTask
from mteb.abstasks.aggregated_task import AbsTaskAggregate, AggregateTaskMetadata
from mteb.overview import get_task

task_list_sts17: list[AbsTask] = [
    get_task(task_name="STS17MultilingualVisualSTS", hf_subsets=["en-en"])
]


class STS17MultilingualVisualSTSEng(AbsTaskAggregate):
    metadata = AggregateTaskMetadata(
        name="VisualSTS17Eng",
        description="STS17MultilingualVisualSTS English only.",
        reference="https://arxiv.org/abs/2402.08183/",
        tasks=task_list_sts17,
        main_score="cosine_spearman",
        type="VisualSTS(eng)",
        bibtex_citation="""@article{xiao2024pixel,
  title={Pixel Sentence Representation Learning},
  author={Xiao, Chenghao and Huang, Zhuoxu and Chen, Danlu and Hudson, G Thomas and Li, Yizhi and Duan, Haoran and Lin, Chenghua and Fu, Jie and Han, Jungong and Moubayed, Noura Al},
  journal={arXiv preprint arXiv:2402.08183},
  year={2024}
}""",
    )


task_list_sts17_multi: list[AbsTask] = [
    get_task(
        task_name="STS17MultilingualVisualSTS",
        hf_subsets=[
            "ko-ko",
            "ar-ar",
            "en-ar",
            "en-de",
            "en-tr",
            "es-en",
            "es-es",
            "fr-en",
            "it-en",
            "nl-en",
        ],
    )
]


class STS17MultilingualVisualSTSMultilingual(AbsTaskAggregate):
    metadata = AggregateTaskMetadata(
        name="VisualSTS17Multilingual",
        description="STS17MultilingualVisualSTS multilingual.",
        reference="https://arxiv.org/abs/2402.08183/",
        tasks=task_list_sts17_multi,
        main_score="cosine_spearman",
        type="VisualSTS(multi)",
        bibtex_citation="""@article{xiao2024pixel,
  title={Pixel Sentence Representation Learning},
  author={Xiao, Chenghao and Huang, Zhuoxu and Chen, Danlu and Hudson, G Thomas and Li, Yizhi and Duan, Haoran and Lin, Chenghua and Fu, Jie and Han, Jungong and Moubayed, Noura Al},
  journal={arXiv preprint arXiv:2402.08183},
  year={2024}
}""",
    )
