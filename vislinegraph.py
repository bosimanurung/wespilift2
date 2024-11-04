import numpy as np
from random import sample
import matplotlib.pyplot as plt
import matplotlib.colors as pltc

class Visualization():
    
    def __init__(self, data):
        self.data           = data
        self.defaultfigsize = (20, 15)
    
    def randomColor(self, limit):
        all_colors = [k for k, v in pltc.cnames.items()]
        for i in ['black', 'white', 'cyan', 'aqua', 'red']:
          all_colors.remove(i)
        colors = sample(all_colors, limit)
        return colorsf
    
    def lineGraph(self, **parameter):
        #Definisikan parameter
        title    = parameter.get('title', '')
        figsize  = parameter.get('figsize', self.defaultfigsize)
        
        fig, ax  = plt.subplots(1, figsize = figsize)
        
        #Buat grafik garisnya
        self.data.plot(figsize = figsize, linestyle = '-', marker = 'o', ax = ax)

        # bsadded 4Okt2024 - set grid
        plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

        #Hapus garis tepi di atas dan kanan
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        
        #Set judul grafik 
        ax.set_title(title, fontsize = 20)
        ax.legend(prop={'size': 15})
    
        #ax.set_xlabel('Flow rate, Q (BFPD)', labelpad = 12, fontsize = 15)
        #ax.set_ylabel('Pressure (psi)', labelpad = 12, fontsize = 15)        
        ax.set_xlabel('Pressure (psi)', labelpad = 12, fontsize = 15)
        ax.set_ylabel('Flow rate, Q (BFPD', labelpad = 12, fontsize = 15)        

        return fig, ax

    def bubbleGraph(self, **parameter):
        data     = self.data
        annotate = parameter.get('annotate')
        area     = parameter.get('area')
        title    = parameter.get('title', '')
        figsize  = parameter.get('figsize', self.defaultfigsize)
        colors   = self.randomColor(data.shape[0])
        
        data = data.sort_values(by = [area], ascending = False).reset_index(drop = True)
        data['annotate'] = (data.index + 1).astype('str') + '. ' + data[annotate[0]] + '\n' + data[annotate[1]]
        
        bubble_chart = BubbleChart(area = data[area], bubble_spacing = 0)
        bubble_chart.collapse()

        fig, ax = plt.subplots(subplot_kw = dict(aspect = "equal"))
        fig.set_size_inches(figsize[0], figsize[1])
        bubble_chart.plot(ax, data['annotate'], colors)
        ax.axis("off")
        ax.relim()
        ax.autoscale_view()
        ax.set_title(title, fontsize = 25)

        return fig, ax

class BubbleChart:
    def __init__(self, area, bubble_spacing=0):
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bubbles = np.ones((len(area), 4))
        self.bubbles[:, 2] = r
        self.bubbles[:, 3] = area
        self.maxstep = 2 * self.bubbles[:, 2].max() + self.bubble_spacing
        self.step_dist = self.maxstep / 2

        length = np.ceil(np.sqrt(len(self.bubbles)))
        grid = np.arange(length) * self.maxstep
        gx, gy = np.meshgrid(grid, grid)
        self.bubbles[:, 0] = gx.flatten()[:len(self.bubbles)]
        self.bubbles[:, 1] = gy.flatten()[:len(self.bubbles)]

        self.com = self.center_of_mass()

    def center_of_mass(self):
        return np.average(self.bubbles[:, :2], axis=0, weights=self.bubbles[:, 3])

    def center_distance(self, bubble, bubbles):
        return np.hypot(bubble[0] - bubbles[:, 0], bubble[1] - bubbles[:, 1])

    def outline_distance(self, bubble, bubbles):
        center_distance = self.center_distance(bubble, bubbles)
        return center_distance - bubble[2] - \
            bubbles[:, 2] - self.bubble_spacing

    def check_collisions(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        return len(distance[distance < 0])

    def collides_with(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        idx_min = np.argmin(distance)
        return idx_min if type(idx_min) == np.ndarray else [idx_min]

    def collapse(self, n_iterations = 50):
        for _i in range(n_iterations):
            moves = 0
            for i in range(len(self.bubbles)):
                rest_bub = np.delete(self.bubbles, i, 0)
                dir_vec = self.com - self.bubbles[i, :2]
                dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))

                new_point = self.bubbles[i, :2] + dir_vec * self.step_dist
                new_bubble = np.append(new_point, self.bubbles[i, 2:4])

                if not self.check_collisions(new_bubble, rest_bub):
                    self.bubbles[i, :] = new_bubble
                    self.com = self.center_of_mass()
                    moves += 1
                else:
                    for colliding in self.collides_with(new_bubble, rest_bub):
                        dir_vec = rest_bub[colliding, :2] - self.bubbles[i, :2]
                        dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))
                        orth = np.array([dir_vec[1], -dir_vec[0]])
                        new_point1 = (self.bubbles[i, :2] + orth *
                                      self.step_dist)
                        new_point2 = (self.bubbles[i, :2] - orth *
                                      self.step_dist)
                        dist1 = self.center_distance(
                            self.com, np.array([new_point1]))
                        dist2 = self.center_distance(
                            self.com, np.array([new_point2]))
                        new_point = new_point1 if dist1 < dist2 else new_point2
                        new_bubble = np.append(new_point, self.bubbles[i, 2:4])
                        if not self.check_collisions(new_bubble, rest_bub):
                            self.bubbles[i, :] = new_bubble
                            self.com = self.center_of_mass()

            if moves / len(self.bubbles) < 0.1:
                self.step_dist = self.step_dist / 2

    def plot(self, ax, labels, colors):
        for i in range(len(self.bubbles)):
            circ = plt.Circle(self.bubbles[i, :2], self.bubbles[i, 2], color = colors[i])
            ax.add_patch(circ)
            ax.text(*self.bubbles[i, :2], labels[i], horizontalalignment='center', verticalalignment='center', fontsize = 14)


