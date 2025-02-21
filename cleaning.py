import os
import os.path as osp
import pandas as pd
from pandas.io.common import _NA_VALUES

user_na_values = _NA_VALUES - {'NULL', 'null', 'nan', 'NaN'}


def get_users_for_episode_count_ban(animelists: pd.DataFrame):
    users_for_ban = pd.Series(animelists[animelists['my_watched_episodes'] == 65535]['username'].unique())
    return users_for_ban


def get_users_for_episode_count_ban_cached():
    cache_name = 'cache_users-to-ban.csv'
    if osp.isfile(cache_name):
        users_for_ban = pd.read_csv(cache_name, encoding='utf-8', na_values=user_na_values, keep_default_na=False)
        return users_for_ban

    print('cache not found, loading and calculating, may take quite long')
    animelists = pd.read_csv('animelists_filtered.csv', na_values=user_na_values, keep_default_na=False)
    users_for_ban = get_users_for_episode_count_ban(animelists)
    users_for_ban.to_csv(cache_name, index=False, sep=',', encoding='utf-8')
    return users_for_ban


def get_user_days_spent_watching_cached():
    cache_name = 'cache_user_days_spent_watching.csv'
    if osp.isfile(cache_name):
        user_day_spent_watching = pd.read_csv(cache_name, index_col=0, encoding='utf-8', na_values=user_na_values,
                                              keep_default_na=False)
        return user_day_spent_watching

    raise Exception('cache not found, must run the basic_cleanup_animelists.ipynb')


def get_users_last_list_update_cached():
    cache_name = 'cache_users_last_list_update.csv'
    if osp.isfile(cache_name):
        users_last_list_update = pd.read_csv(cache_name, index_col=0, encoding='utf-8', na_values=user_na_values,
                                             keep_default_na=False)
        return users_last_list_update

    raise Exception('cache not found, must run the basic_cleanup_animelists.ipynb')


def get_users_stats_episodes_cached():
    cache_name = 'cache_users_stats_episodes.csv'
    if osp.isfile(cache_name):
        users_stats_episodes = pd.read_csv(cache_name, index_col=0, encoding='utf-8', na_values=user_na_values,
                                           keep_default_na=False)
        return users_stats_episodes

    raise Exception('cache not found, must run the basic_cleanup_animelists.ipynb')


def get_usernames_to_keep_cached():
    cache_name = 'cache_usernames_after_filtering.csv'
    if osp.isfile(cache_name):
        usernames_to_keep = pd.read_csv(cache_name, index_col=0, encoding='utf-8', na_values=user_na_values,
                                        keep_default_na=False)
        return usernames_to_keep

    raise Exception('cache not found, must run the basic_cleanup_animes_and_users.ipynb')


def get_anime_ids_after_username_clear_cached():
    cache_name = 'cache_anime_ids_after_username_clear.csv'
    if osp.isfile(cache_name):
        anime_ids_to_keep = pd.read_csv(cache_name, encoding='utf-8')
        return anime_ids_to_keep

    raise Exception('cache not found, must run the basic_cleanup_animelists.ipynb')


def get_anime_ids_after_cleaning_cached():
    cache_name = 'cache_anime_ids_after_cleaning.csv'
    if osp.isfile(cache_name):
        anime_ids_to_keep = pd.read_csv(cache_name, encoding='utf-8')
        return anime_ids_to_keep

    raise Exception('cache not found, must run the basic_cleanup_animes_and_users.ipynb')
