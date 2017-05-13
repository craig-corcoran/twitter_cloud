# -*- coding: utf-8 -*-
import click
from .tweet_cloud import tweet_cloud


@click.command()
@click.option('--user', default="realDonaldTrump", help='twitter account name')
@click.option('--count', default=200, help='number of most recent tweets')
@click.option('--img_filename', default='wordcloud.png', help='file name for output word cloud image')
def main(user, count, img_filename):
    ''' working with twitter
    '''
    tweet_cloud(user=user, count=count, img_filename=img_filename)
