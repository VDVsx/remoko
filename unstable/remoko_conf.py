#
#      remoko_conf.py
#
#      Copyright 2008 -2009 Valerio Valerio <vdv100@gmail.com>
#						
#
#      This program is free software; you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation; either version 2 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program; if not, write to the Free Software
#      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#


import ConfigParser
import os
import os.path

defaultsfile = "/etc/remoko/remoko.cfg"


class remoko_conf:

	def __init__(self):

		self.config = ConfigParser.ConfigParser()
		try:
			self.config.readfp(open(defaultsfile))

		except:
			os.system("mkdir /etc/remoko/")
			#os.system("cp /usr/share/remoko/data/remoko.cfg /etc/remoko/")
			os.system("cp data/remoko.cfg /etc/remoko/")
			self.config.readfp(open(defaultsfile))

		#settings
		self.fullscreen = self.config.get("user","fullscreen")
		self.scroll = self.config.get("user","scroll")
		self.accelerometer = self.config.get("user","accelerometer")
		#presentation profile
		self.previous_key = self.config.get("presentation","previous_key")
		self.next_key = self.config.get("presentation","next_key")
		self.fullscreen_key = self.config.get("presentation","fullscreen_key")
		self.no_fullscreen_key = self.config.get("presentation","no_fullscreen_key")
		#multimedia profile
		self.play_key = self.config.get("multimedia","play_key")
		self.pause_key = self.config.get("multimedia","pause_key")
		self.stop_key = self.config.get("multimedia","stop_key")
		self.forward_key = self.config.get("multimedia","forward_key")
		self.backward_key = self.config.get("multimedia","backward_key")
		self.fullscreen_key_m = self.config.get("multimedia","fullscreen_key_m")
		self.volume_m_key = self.config.get("multimedia","volume_m_key")
		self.volume_p_key = self.config.get("multimedia","volume_p_key")
		self.no_fullscreen_key_m = self.config.get("multimedia", "no_fullscreen_key_m")
		#accelerometer profile
		self.up_key = self.config.get("accelerometer","up_key")
		self.up_down_key = self.config.get("accelerometer","up_down_key")
		self.right_key = self.config.get("accelerometer","right_key")
		self.right_left_key = self.config.get("accelerometer","right_left_key")
		self.left_key = self.config.get("accelerometer","left_key")
		self.left_right_key = self.config.get("accelerometer","left_right_key")
		self.down_key = self.config.get("accelerometer","down_key")
		self.down_up_key = self.config.get("accelerometer","down_up_key")
		self.forw_backw_key = self.config.get("accelerometer", "forw_backw_key")
		self.shake_shake_key = self.config.get("accelerometer","shake_shake_key")
		self.z_key = self.config.get("accelerometer","z_key")
		self.horizontal_circle_key = self.config.get("accelerometer", "horizontal_circle_key")
		#games profile
		self.up_key = self.config.get("games","up_key")
		self.down_key = self.config.get("games","down_key")
		self.right_key = self.config.get("games","right_key")
		self.left_key = self.config.get("games","left_key")
		self.a_key = self.config.get("games", "a_key")
		self.b_key = self.config.get("games","b_key")
		self.c_key = self.config.get("games","c_key")
		self.d_key = self.config.get("games", "d_key")
						
					
	def set_option(self,seccion,opt,value):
		
		self.config.set(seccion,opt, value)
		print "conf set"
		
	def save_options(self):	
	
		try:
			
			file = open(defaultsfile, 'w')
			self.config.write(file)
			file.close()
			print "Options saved"
			
		except:
			
			print "Error: Non such file or directory \'" + defaultsfile + "\'"

		
