#
#      remoko_presentation.py
#
#      Copyright 2008 -2009 	Valerio Valerio <vdv100@gmail.com>
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


import e_dbus
import evas
import evas.decorators
import edje
import edje.decorators
import ecore
import ecore.x
import ecore.evas
from remoko_edje_group import *

#----------------------------------------------------------------------------#
class presentation(edje_group):
#----------------------------------------------------------------------------#
    def __init__(self, main):
        edje_group.__init__(self, main, "presentation")

    def onShow( self ):
	self.focus = True
    

    def onHide( self ):
	self.focus = False

    @edje.decorators.signal_callback("mouse,up,1", "*")
    def on_edje_signal_button_released(self, emission, source):

	if source =="back" or source == "conf_keys":
		pass
	else:
		self.main.connection.release_keyboard_event()

    @edje.decorators.signal_callback("mouse,clicked,1", "*")
    def on_edje_signal_button_pressed(self, emission, source):
	if source == "back":
		
		self.main.transition_to("menu")

	elif source ==	"conf_keys":
		
		self.main.transition_to("presentation_conf")
	
	elif source == "conf_gestures":

		self.main.accelerometer_prev = "presentation"
		self.main.transition_to("accelerometer_conf")

	elif source == "previous":


		key = self.main.previous_key
		modif, val = key_dec(self,key)
		
		self.main.connection.send_keyboard_event(modif,val)

	elif source == "next":

		key = self.main.next_key
		modif, val = key_dec(self,key)

		self.main.connection.send_keyboard_event(modif,val)

	elif source == "fullscreen":

		key = self.main.fullscreen_key
		modif, val = key_dec(self,key)

		self.main.connection.send_keyboard_event(modif,val)

	elif source == "no_fullscreen":

		key = self.main.no_fullscreen_key
		modif, val = key_dec(self,key)

		self.main.connection.send_keyboard_event(modif,val)

#----------------------------------------------------------------------------#
class presentation_conf(edje_group):
#----------------------------------------------------------------------------#
    def __init__(self, main):
        edje_group.__init__(self, main, "presentation_conf")
	count = 0
	self.prev_key = ""
	self.next_key = ""
	self.full_key = ""
	self.no_full_key = ""
	for i in (self.main.previous_key,self.main.next_key,self.main.fullscreen_key, self.main.no_fullscreen_key):
		if len(i) > 6:
			#shift translation
			if i[0] == "s":
				text_value = self.main.key_mapper.mapper[i]
				count +=1
		else:
			text_value = i
			count +=1
		if count == 1:
			self.prev_key = text_value
		elif count == 2:
			self.next_key = text_value
		elif count == 3:
			self.full_key = text_value
		elif count == 4:
			self.no_full_key = text_value
				
		 
	self.part_text_set("previous_key_icon", self.prev_key)
	self.part_text_set("next_key_icon", self.next_key)
	self.part_text_set("fullscreen_key_icon", self.full_key)
	self.part_text_set("no_fullscreen_key_icon", self.no_full_key)
	self.key_value = ""

    @edje.decorators.signal_callback("mouse,clicked,1", "*")
    def on_edje_signal_button_pressed(self, emission, source):
	if source == "back":
		self.main.remoko_conf.save_options()
		self.main.transition_to("presentation")	
	else:
		if source == "previous_key":

			self.key_value = self.part_text_get("previous_key_icon")
			self.main.key_text = self.key_value

		elif source == "next_key":

			self.key_value = self.part_text_get("next_key_icon")
			self.main.key_text = self.key_value

		elif source == "fullscreen_key":

			self.key_value = self.part_text_get("fullscreen_key_icon")
			self.main.key_text = self.key_value

		elif source == "no_fullscreen_key":

			self.key_value = self.part_text_get("no_fullscreen_key_icon")
			self.main.key_text = self.key_value

		self.main.current_conf_screen = "presentation"
		self.main.current_source = source
		self.main.groups["conf_keys"].part_text_set("value"," "+self.key_value+ " ")
		self.main.transition_to("conf_keys")	
	

