# -*- coding: utf-8 -*-

"""
@author: Siying Liu
"""

import Analysis.CalcMinMax as AnaOper
import DataCleaning.DeleteNull as DataOper
import FileSystem.LoadCSVFile as FileOper
from Visualization.ShowPlot import ShowHistogram

FileName = 'Data/base.csv'

FileData = FileOper.LoadFile(FileName)
FileData = DataOper.ReplaceNullData(FileData, 0)
MeanRes = AnaOper.CalcMean(FileData)
ShowHistogram(FileData)
