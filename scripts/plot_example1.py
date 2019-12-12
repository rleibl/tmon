
from matplotlib import pyplot as plt
import datetime
import sqlite3


def plot(filename, temps, times):
    # plot with date on x-axis
    plt.plot_date(times, temps, 'b-')

    # set limits for axes (otherwise automatically calculated)
    plt.ylim(20, 30)
    #plt.xlim(?)

    # regular plot
    #plt.plot(temp)

    # label axes
    plt.xlabel("Time")
    plt.ylabel("Temp")

    # show or save image
    #plt.show()
    plt.savefig(filename)


conn = sqlite3.connect("example.sqlite3")
c = conn.cursor()


q = ("SELECT node, time, temp FROM temperature WHERE time > ?")

# week
delta = datetime.timedelta(weeks=1)
t = datetime.datetime.now() - delta
print(str(t))

c.execute(q, (t,))
r = c.fetchall()

ti = [ a[1] for a in r ]
te = [ a[2] / 1000 for a in r ]

plot("out_week.png", te, ti)
