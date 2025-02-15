from context import campaignadvisor
import pandas as pd
import matplotlib.pyplot as pyplot


def plot_columns(df, x_column, y_column):
    df.plot(kind='scatter', x=x_column, y=y_column)
    pyplot.show()


def main():
    pd.options.display.max_rows = 1000
    county_statistics_name = campaignadvisor.dataframe_holder.COUNTY_STATISTICS
    county_statistics = campaignadvisor.dataframe_holder.get_dataframe(county_statistics_name)
    for name in list(county_statistics.columns):
        print name
    corr = county_statistics.corr()
    # Only bother printing correlations involving variables we actually care about
    print corr[['percent_vote_dem', 'percent_vote_gop', 'contribution_median', 'contribution_mean',
                'contribution_count']]

    plot_columns(county_statistics, 'percent_vote_gop', 'Ed4CollegePlusPct0812')

if __name__ == "__main__":
    main()