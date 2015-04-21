# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    UniqueWindow.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaguillo <jaguillo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/04/21 22:45:07 by jaguillo          #+#    #+#              #
#    Updated: 2015/04/22 00:26:12 by juloo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sublime_plugin import EventListener

class JulooUniqueWindow(EventListener):

	window = None

	def on_new_async(self, view):
		self.on_new_window(view)

	def on_activated(self, view):
		self.on_new_window(view)

	def on_new_window(self, view):
		if self.window == None:
			self.window = view.window()
		elif self.window != view.window() and len(view.window().views()) == 0:
			print("Merged new empty window")
			data = self.window.project_data()
			if not "folders" in data:
				data['folders'] = []
			for f in view.window().folders():
				data['folders'].append({"path": f, "follow_symlinks": True})
			self.window.set_project_data(data)
			view.window().run_command("close")

	def on_close(self, view):
		if view.window() == self.window and len(self.window.views()) == 0:
			self.window.new_file()
			print("Prevent this window from closing")
