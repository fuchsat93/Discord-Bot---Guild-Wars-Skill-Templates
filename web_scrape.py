from bs4 import BeautifulSoup
import requests
import urllib
from urllib.parse import urlparse

import numpy as np
import cv2

import PIL
from PIL import Image
import os

import os.path

def skillbar_maker(skill_array):

    cwd = os.getcwd()
    skill_link_array = []

    for w, x in enumerate(skill_array):
        skill_array[w] = skill_array[w].replace(' ', '_')
        if not os.path.isfile(os.getcwd() + '\skillbars\\' + skill_array[w] + '.jpg'):
            if skill_array[w][0] == '\'':
                buffer_string = skill_array[w].replace('\'', '\"', 1)
                buffer_string = buffer_string[::-1].replace('\'', '\"', 1)
                buffer_string = buffer_string[::-1]
                skill_array[w] = buffer_string
            source = requests.get('https://wiki.guildwars.com/wiki/' + skill_array[w]).text
            print(skill_array[w])
            print('https://wiki.guildwars.com/wiki/' + skill_array[w])
            soup = BeautifulSoup(source, 'lxml')

            mydivs = soup.findAll("div", {"class": "skill-image"})

            for div in mydivs:
                links = div.findAll('img')
                for a in links:
                    skill_link = "https://wiki.guildwars.com/" + a['src']

            urllib.request.urlretrieve(skill_link, cwd + '\skillbars\\' + skill_array[w].replace('\"', '\'') + '.jpg')
        skill_link_array.append(cwd + '\skillbars\\' + skill_array[w].replace('\"', '\'') + '.jpg')

    skill_imgs = [PIL.Image.open(i) for i in skill_link_array]

    min_shape = sorted([(np.sum(i.size), i.size) for i in skill_imgs])[0][1]
    imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in skill_imgs))
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save(cwd + '\skillbars\\' + 'skill_template.jpg')
