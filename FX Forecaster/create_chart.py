import mplfinance as mpf


def create_chart_parellel(df_chunk):
    """Function to parallalize the training data (chart) creation"""
    # filtered df to generate images from (30 candles history for each signal)
    
    temp_df = df_chunk
    
    # sort values by date index
    temp_df.sort_index(inplace=True,ascending=True)
    
    # Signal label
    label = temp_df.signal.values[-1]

    # image pre-fix time tag
    date_start = temp_df.index.min().strftime('%Y-%m-%d_%H-%M')    
    
    # image post-fix time tag
    date_predict = temp_df.index.max().strftime('%Y-%m-%d_%H-%M')
    
    # extract curr. pair labels + folder-path
    curr_1 = temp_df.curr_1.unique()[0]
    curr_2 = temp_df.curr_2.unique()[0]
    folder_path = temp_df.f_path.unique()[0]
    
    # path to store image
    image_path = folder_path+'train_imgs/'+f'{curr_1}_{curr_2}_{date_start}_{date_predict}_{label}.jpg'
    
    apds = [mpf.make_addplot(temp_df['ewm_50_h']
                             #, linestyle ='dashdot'
                             , color = 'blue'
                             , alpha = 0.2),
            mpf.make_addplot(temp_df['ewm_50_m']
                             #, linestyle ='dashdot'
                             , color = 'darkblue'
                             , alpha = 0.7),
            mpf.make_addplot(temp_df['ewm_50_l']
                             #, linestyle ='dashdot'
                             , color = 'blue'
                             , alpha = 0.2),
            mpf.make_addplot(temp_df['ewm_200']
                             #, linestyle ='line'
                             , color='red')
           ]

    s  = mpf.make_mpf_style(base_mpf_style='charles'
                            , gridstyle = 'dashed')

    export_image = mpf.plot(temp_df
                            , type = 'candle'
                            , style = s
                            , volume = True
                            , ylabel=''
                            , ylabel_lower=''
                            , figratio = (12,8)
                            , tight_layout = True
                            , addplot = apds
                            , panel_ratios = (6,1)
                            , fill_between = dict(y1 = temp_df['ewm_50_h'].values
                                                  , y2 = temp_df['ewm_50_l'].values
                                                  , alpha=0.2
                                                  , color='b')
                            , scale_width_adjustment = dict(volume=0.7
                                                            , candle=1.2
                                                            , lines=0.3)
                            , savefig=dict(fname=image_path
                                           #, dpi=100
                                           , pad_inches=0.25))
    
    return date_predict # return the date that the signal is predicted 