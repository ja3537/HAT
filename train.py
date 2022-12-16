# flake8: noqa
import os.path as osp
import hat.archs
import hat.data
import hat.models
from basicsr.train import train_pipeline
import time

if __name__ == '__main__':
    print("starting training")
    start = time.time()
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    train_pipeline(root_path)
    end = time.time()
    print("done")
    print("{:.3f}".format(end-start))
