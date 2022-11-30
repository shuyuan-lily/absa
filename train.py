from pyabsa.functional import ATEPCModelList
from pyabsa.functional import Trainer, ATEPCTrainer
from pyabsa.functional import ABSADatasetList
from pyabsa.functional import ATEPCConfigManager

config = ATEPCConfigManager.get_atepc_config_english()
config.model = ATEPCModelList.FAST_LCF_ATEPC
config.evaluate_begin = 0
config.log_step = -1
config.batch_size = 16
config.num_epoch = 30
config.max_seq_len = 128
config.cache_dataset = False
config.use_bert_spc = True
config.l2reg = 1e-5
config.learning_rate = 1e-5
config.pretrained_bert = 'yangheng/deberta-v3-base-absa-v1.1'
Dataset = "datasets/atepc_datasets/170.LargerCustom"

checkpoint_path = 'checkpoints/fast_lcf_atepc_custom_dataset_cdw_apcacc_87.04_apcf1_80.44_atef1_82.27'
# correct usage offered by author: 'lcfs_atepc_cdw_apcacc_86.17_apcf1_58.3_atef1_70.86'

aspect_extractor = Trainer(config=config,
                           dataset=Dataset,
                           checkpoint_save_mode=1,
                           from_checkpoint=checkpoint_path,
                           auto_device=True,
                           load_aug=True
                           ).load_trained_model()

aspect_extractor.extract_aspect(
    ['the wine list is incredible and extensive and diverse , the food is all incredible and the staff was all very nice , ood at their jobs and cultured .',
     'the International Rice Research Institute (IRRI) based in the Philippines have been working on The tests for a long time and the International Rice Research Institute (IRRI) based in the Philippines would like to have The tests completed as soon as possible,', 
     'So the 75 percent falls far short of what a tobacco farmer needs. The Zimbabwe Tobacco Association (ZTA) are also of the view that tobacco is the biggest foreign currency earner yet The Zimbabwe Tobacco Association (ZTA) were awarded the lowest retention when other sectors have been given between 80 to 100 percent,']
)
