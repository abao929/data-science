"""
In this file, we'll do some sample code to plot some graphs and to utilize the functions in
utils.py!
"""
# This line is to import all functions and variables in utils.py
from utils import *
import random
import numpy as np
import pandas as pd

# import matplotlib - very important
import matplotlib.pyplot as plt

# import the toolkit for plotting matplotlib 3D
from mpl_toolkits import mplot3d

# import the stuff for geographic plots
import plotly.figure_factory as ff


#################################### EXAMPLE GRAPHS ####################################

def plot_two_lines_one_graph():
    """
    Example to draw multiple lines on one graph
    """
    # just constructing some dummy data
    line_one_ys = [e + random.randint(0, 10) for e in range(50)]
    line_two_ys = [e + random.randint(0, 10) for e in np.array(range(50))[::-1]]
    Xs = list(range(50))

    # alright. construct our Figure and Axes (refer to lab)
    fig, ax = plt.subplots()


    # plotting line 1 - color = "orange"
    ax.plot(Xs, line_one_ys, "orange")

    # plotting line 2 - color = "blue"
    ax.plot(Xs, line_two_ys, "blue")

    # setting labels
    ax.set_xlabel("x values")
    ax.set_ylabel("y values")
    ax.set_title("stonks and reverse stonks!")

    plt.show()
    

def plot_two_graphs_one_fig():
    """
    Example function to draw multiple graphs on one matplotlib figure
    
    Some more examples with more rows:
    https://www.geeksforgeeks.org/plot-multiple-plots-in-matplotlib/
    """
    # just constructing some dummy data
    graph_one_ys = [e + random.randint(0, 10) for e in range(50)]
    graph_two_ys = [e + random.randint(0, 10) for e in np.array(range(50))[::-1]]

    # alright. construct our Figure and Axes (refer to lab)
    fig, ax = plt.subplots(1, 2) # creating the space for 1 row and 2 columns of graphs
    
    # construct the dummy x values
    Xs = list(range(50))
    assert len(Xs) == len(graph_one_ys) == len(graph_two_ys)

    # for the position 1, plot graph one
    ax[0].plot(Xs, graph_one_ys)
    # set title at row 1 col 1
    ax[0].set_title("stonks!")
    # set x and y labels
    ax[0].set_xlabel("x units")
    ax[0].set_ylabel("y values")

    # for the position 2, plot graph 2
    ax[1].plot(list(range(50)), graph_two_ys)
    # set title at row 1 col 1
    ax[1].set_title("reverse stonks!")
    # set x and y labels
    ax[1].set_xlabel("x units")
    ax[1].set_ylabel("y values")

    plt.show()


def plot_multiclass_fig_2D():
    """
    Example function to plot 2D points with colors
    """
    ### construct the dataframe that we'll plot
    df = pd.DataFrame()
    df["x"] = [random.randint(0, 100)/100.0 for e in range(50)]
    df["y"] = [random.randint(0, 100)/100.0 for e in range(50)]
    # function to generate random label
    def gen_label():
        rand_val = random.randint(0, 100)
        if rand_val <= 33:
            return "A"
        if rand_val <= 66:
            return "B"
        return "C"
    
    df["label"] = [gen_label() for e in range(50)]

    ### plot the graph:
    fig, ax = plt.subplots()
    
    # define the color mapping
    color_mapping = {
        "A": "red",
        "B": "blue",
        "C": "orange"
    }

    # for each class
    for cls in ["A", "B", "C"]:
        # get the examples of that class
        examples = df[df["label"] == cls].to_numpy()
        # and then plot it with the color of our liking
        Xs = examples[:, 0] # get all rows from column 0
        Ys = examples[:, 1] # get all rows from column 1
        ax.scatter(Xs, Ys, c=color_mapping[cls]) # c: color

    # title, axes
    ax.set_title("My 3-class colorful graph!")
    ax.set_xlabel("x values")
    ax.set_ylabel("y values")
    
    plt.show()
    
    
def plot_fig_3D():
    """
    More examples of 3D plots:
    https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
    """
    ### construct the dataframe that we'll plot
    df = pd.DataFrame()
    df["x"] = [random.randint(0, 100)/100.0 for e in range(50)]
    df["y"] = [random.randint(0, 100)/100.0 for e in range(50)]
    df["z"] = [random.randint(0, 100)/100.0 for e in range(50)]

    ### alright, now create the Figures and Axes -- this time its a lil
    # different from just plt.subplots()
    fig = plt.figure()
    ax = plt.axes(projection='3d') # Creating a 3D axes instead of 2D like usual

    # alright, now plot a 3D scatterplot
    ax.scatter3D(df["x"], df["y"], df["z"])

    # and then you can also draw some three dimensional line as well! let's
    # draw a green line
    line_z = np.linspace(0, 15, 1000) # constructing the z coordinates of our line
    line_x, line_y = np.sin(line_z), np.cos(line_z) # constructing the x and y coordinates of our line
    
    ax.plot3D(line_x, line_y, line_z, "green")

    plt.show()


def plot_linear_line():
    """
    Example to draw a line on top of a scatterplot

    More examples on cool lines:
    https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html
    """
    # Construct Xs and Ys for the scatter plot
    xs, ys = np.array([random.randint(0, 100)/100.0 for e in range(50)]),\
                np.array([random.randint(0, 100)/100.0 for e in range(50)])

    # alright, scatter plot the points
    fig, ax = plt.subplots()
    ax.scatter(xs, ys)

    # alright, now draw a solid red line of the function 2x - 1 
    ax.plot(xs, 2*xs - 1, '-r')
    
    plt.show()


def plot_linear_plane():
    """
    Example to draw a 3D linear plane
    """
    ##### CREATING THE VALUES TO PLOT THE 3D PLANE #####
    # create the x and y values - you can read more on np.meshgrid here:
    # https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy

    # the point that the plane is going through
    point1 = np.array([10, 20, 30])

    # we are trying to plot the plane a*x + b*y + c*z + d = 0.
    # define a, b, c:
    coefs = np.array([6, 3, 2])

    # and get the corresponding d value
    d = -point1.dot(coefs)

    # alright, now we will plot it for xs and ys from 0 to 9
    xs, ys = np.meshgrid(range(10), range(10))

    # create the corresponsing z values based on the coefs we found [a, b, c, d]
    zs = ((-coefs[0]*xs -coefs[1]*ys -d) * 1)/coefs[2]

    ## alright, now that we've got xs, ys and zs, we go to the meat
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    # alpha defines how transparent the plane/surface will be
    ax.plot_surface(xs, ys, zs, alpha=0.2)

    plt.show()


def plot_county_counts():
    """
    Plot county count graphs

    Example extracted from plotly documentation: https://plotly.com/python/county-choropleth/
    (Please check this out ^ it will be tremendously helpful)
    """
    # fips of counties in California
    fips = ['06021', '06023', '06027', '06029', '06033', '06059', '06047', '06049', '06051', '06055', '06061']
    # random values associated with each counties
    values = [random.randint(0, 100) for e in fips]

    # create the choropleth graph
    fig = ff.create_choropleth(fips=fips,\
                            values=values,\
                            scope=['CA', 'AZ', 'Nevada', 'Oregon', ' Idaho'],\
                            title='California counties and Nearby States',\
                            legend_title='Values by County'
                            )

    fig.layout.template = None

    fig.show()




############################### EXAMPLE CALLS TO UTILS.PY ###############################

def default_ml_model_calls():
    # Defalt model calls - view the definitions of the functions in `utils.py` to see what the definition
    # of "default" is for each dataset
    for model_name in ["decision_tree", "logistic_regression", "dummy"]: # dummy: baseline model
        for dataset_name in ["ri_traffic_stops", "banknote_authentication"]:
            # Get the trained model (trained on train_df)
            model, one_hot_encoder, train_df, test_df = get_trained_model(dataset_name=dataset_name,\
                                                                            model_name=model_name)

            # Getting the training accuracy, model's predictions and the training targets
            training_acc, training_preds, training_targs = get_model_accuracy(model=model,\
                                                                                df=train_df,\
                                                                                one_hot_encoder=one_hot_encoder,\
                                                                                dataset_name=dataset_name)

            # You can comment/uncomment this section to print out the accuracy
            testing_acc, testing_preds, testing_targs = get_model_accuracy(model=model,\
                                                                            df=test_df,\
                                                                            one_hot_encoder=one_hot_encoder,\
                                                                            dataset_name=dataset_name)

            print(f"\n\n----- DEFAULT: ACCURACY FOR MODEL {model_name} TRAINED ON DATASET {dataset_name}-----\n\n")
            print(f"Training accuracy: {training_acc}")
            print(f"Testing accuracy: {testing_acc}")


def customized_ml_model_call():
    # Customized model calls
    
    # Ex: "I just want to use `stop_duration`, `driver_race`, and `county_fips` as features to predict `is_arrested` using
    # decision tree - on dataset_name = "ri_traffic_stops"
    dataset_name = "ri_traffic_stops"
    model_name = "decision_tree"
    target_name = "is_arrested"
    feature_names = ["stop_duration", "driver_race", "county_fips"]
    trained_tree, one_hot_encoder, train_df, test_df = get_trained_model(dataset_name=dataset_name,\
                                                                        model_name=model_name,\
                                                                        target_name=target_name,\
                                                                        feature_names=feature_names)

    # Getting the training accuracy, model's predictions and the training targets
    training_acc, training_preds, training_targs = get_model_accuracy(model=trained_tree,\
                                                                        df=train_df,\
                                                                        one_hot_encoder=one_hot_encoder,\
                                                                        dataset_name=dataset_name,\
                                                                        target_name=target_name,\
                                                                        feature_names=feature_names)

    # You can comment/uncomment this section to print out the accuracy
    testing_acc, testing_preds, testing_targs = get_model_accuracy(model=trained_tree,\
                                                                    df=test_df,\
                                                                    one_hot_encoder=one_hot_encoder,\
                                                                    dataset_name=dataset_name,\
                                                                    target_name=target_name,\
                                                                    feature_names=feature_names)

    print(f"\n\n----- Custom Decision Tree: ACCURACY FOR MODEL {model_name} TRAINED ON DATASET {dataset_name}-----\n\n")
    print(f"Features: {feature_names}")
    print(f"Training accuracy: {training_acc}")
    print(f"Testing accuracy: {testing_acc}")


def get_datasets():
    # Getting the RI Traffic Stops dataset (Pandas DataFrame):
    ri_traffic_stops = get_ri_stops_df()

    print("RI Traffic Stops Data: ")
    print(ri_traffic_stops)

    # Getting the bank note DataFrame:
    banknote_auth = get_banknote_df()
    
    print("Banknote Authentication Data: ")
    print(banknote_auth)
    


if __name__ == "__main__":
    ## TODO: Uncomment the function calls below and call `python3 sample.py` to visualize - this
    ## is to help you tinker around and help you understand how to graph things / how to use our
    ## helper ML Functions (without having to create your own -- you totally can if you want to though)

    ##### SECTION 0: GETTING DATA EXAMPLES #####
    
    # get_datasets() # TODO: Comment/Uncomment me!!

    ##### SECTION 1: GRAPH EXAMPLES #####

    # plot_two_lines_one_graph() # TODO: Comment/Uncomment me!!
    # plot_two_graphs_one_fig() # TODO: Comment/Uncomment me!!
    # plot_multiclass_fig_2D() # TODO: Comment/Uncomment me!!
    # plot_fig_3D() # TODO: Comment/Uncomment me!!
    # plot_linear_line() # TODO: Comment/Uncomment me!!
    # plot_linear_plane() # TODO: Comment/Uncomment me!!
    # plot_county_counts() # TODO: Comment/Uncomment me!!

    ##### SECTION 2: ML MODEL EXAMPLES #####

    # default_ml_model_calls() # TODO: Comment/Uncomment me!!
    # customized_ml_model_call() # TODO: Comment/Uncomement me!!
    
    print("Please go into sample.py and check out some examples of how to do things!!")