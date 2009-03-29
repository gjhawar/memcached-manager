import matplotlib
matplotlib.use('QT4Agg')
from matplotlib import pyplot

from PyQt4 import QtGui
from PyQt4 import QtCore
from Dialogs.ui_LiveStats import Ui_liveStatsDialog
import time
import threading
import Settings
import os
import datetime

class Dialog(QtGui.QDialog, Ui_liveStatsDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.currentCluster = None
		self.monitor = False
		self.thread = None
		self.threadInterupt = False
		self.stats = []
		
		self.settings = Settings.Settings()
		
		self.connect(self, QtCore.SIGNAL('finished(int)'), self.stopMonitor)
		
	def show(self):
		QtGui.QDialog.show(self)
		self.startMonitor()
		self.stats = []
		
	def setCluster(self, cluster):
		self.currentCluster = cluster
		
	def startMonitor(self):
		print "Start Monitor"
		self.monitor = True
		self.threadInterupt = False
		if self.thread is None:
			self.thread = Monitor(self)
			self.connect(self.thread, QtCore.SIGNAL('refresh'), self.updateGraphs)
			self.thread.start()
	
	def stopMonitor(self):
		print "Stop Monitor"
		self.monitor = False
		self.threadInterupt = True
		self.stats = []
		
	def toggleMonitor(self):
		if self.monitor:
			self.stopMonitor()
		else:
			self.startMonitor()
			
	def updateGraphs(self):
		print 'Refresh'
		self.graphConnections()
		self.graphGetsSets()
		self.graphHistMisses()
		self.graphMemory()
			
	def graphConnections(self):
		figure = pyplot.figure(figsize=(5.5,2.51), linewidth=2)
		matplotlib.rc('lines', linewidth=2)
		matplotlib.rc('font', size=10)
		
		y = []
		legend = ['Total']
		for s in self.stats[0]['stats'].getServers():
			legend.append(s.getName())
			
		for s in self.stats:
			values = []
			values.append(s['stats'].getConnections())
			for server in s['stats'].getServers():
				values.append(server.getConnections())
			y.append(values)
			
		ax = figure.add_subplot(111)
		#TODO: Added Preference Values for Colors
		#ax.set_color_cycle(['c', 'm', 'y', 'k'])
		ax.plot(y)
		
		def format_date(x, pos=None):
			return self.stats[int(x)]['date'].strftime('%I:%M:%S')
		ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(format_date))
		ax.legend(legend, prop=matplotlib.font_manager.FontProperties(size=8))
		figure.autofmt_xdate()
		
		path = os.path.join(Settings.getSaveLocation(), 'ActiveConnections.png')
		figure.savefig(path)
		self.lblConnectionsGraph.setPixmap(QtGui.QPixmap(path))
	
	def graphGetsSets(self):
		pass
	
	def graphHistMisses(self):
		pass
	
	def graphMemory(self):
		pass
		
			
#class Monitor(threading.Thread):
class Monitor(QtCore.QThread):
	def __init__(self, dialog):
		#threading.Thread.__init__(self)
		QtCore.QThread.__init__(self)
		self.dialog = dialog
		
	def run(self):
		while not self.dialog.threadInterupt:
			stats = self.dialog.currentCluster.getStats()
			self.dialog.stats.append({'date':datetime.datetime.today().time(), 'stats':stats})
			if len(self.dialog.stats) > 20:
				self.dialog.stats.pop(0)
				
			self.emit(QtCore.SIGNAL('refresh'), None)
			time.sleep(int(self.dialog.settings.settings.config['Stats']['RefreshInterval']))