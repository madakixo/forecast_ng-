import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def visualize_forecast(df, combined):
    """Visualize the forecast results."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    line, = ax1.plot([], [], lw=2, label='Predicted')
    ax1.plot(df.index, df['feature1'], label='Actual', alpha=0.5)
    ax1.set_ylim(0, max(df['feature1']) * 1.1)
    ax1.set_xlim(df.index.min(), df.index.max() + pd.to_timedelta('30D'))
    ax1.set_title('Actual vs Predicted Values')
    ax1.legend()

    ax2.plot(combined.index, abs(combined['actual'] - combined['predicted']), label='Error')
    ax2.set_title('Prediction Errors Over Time')
    ax2.set_ylabel('Absolute Error')
    ax2.legend()

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        new_dates = combined.index[:i].tolist()
        new_data = combined['predicted'].iloc[:i].tolist()
        line.set_data(new_dates, new_data)
        ax1.set_xlim(df.index.min(), max(new_dates, default=df.index.max()))
        return line,

    anim = FuncAnimation(fig, animate, init_func=init, frames=len(combined), interval=200, blit=True)
    plt.show()
