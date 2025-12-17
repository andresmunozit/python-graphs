import matplotlib.pyplot as plt
import numpy as np

# Set the global font to be 'sans-serif' (Arial, Helvetica, etc.), size 11
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

output_file = '/output/plot.png'

# Defining the technologies and corresponding years of experience
tech_experience = {
    'JavaScript': 7,
    'TypeScript': 6,
    'NestJS': 2,
    'Node.js': 6,
    'Express': 5,
    'TypeORM': 2,
    'GraphQL': 1,
    'Golang': 2,
    'Gin': 2,
    'Gorm': 2,
    'Bash': 4,
    'PostgreSQL': 3,
    'MongoDB': 1,
    'Redis': 2,
    'NATS': 1,
    'Kafka': 3,
    'RabbitMQ': 2,
    'Git': 5,
    'GitLab': 4,
    'GitHub': 3,
    'Docker': 4,
    'Kubernetes': 3,
    'DataDog': 2,
    'Prometheus': 3,
    'Grafana': 3,
    'AWS': 3,
    'GCP': 2,
    'Azure': 1,
}

groups = {
    'JavaScript': 'Languajes',
    'Golang': 'Languajes',
    'TypeScript': 'Languajes',
    'Bash': 'Languajes',
    'Node.js': 'Utilities', 
    'Express': 'Utilities',
    'NestJS': 'Utilities',
    'TypeORM': 'Utilities',
    'GraphQL': 'Utilities',
    'Gin': 'Utilities',
    'Gorm': 'Utilities',
    'MongoDB': 'Databases',
    'PostgreSQL': 'Databases',
    'Redis': 'Databases',
    'NATS': 'Microservices',
    'Kafka': 'Microservices',
    'RabbitMQ': 'Microservices',
    'Git': 'GitOps',
    'GitLab': 'GitOps',
    'GitHub': 'GitOps',
    'Linux': 'DevOps',
    'Docker': 'DevOps', 
    'Kubernetes': 'DevOps',
    'DataDog': 'Observability',
    'Prometheus': 'Observability',
    'Grafana': 'Observability',
    'AWS': 'Cloud',
    'GCP': 'Cloud',
    'Azure': 'Cloud',
}

# Grouping related technologies and defining colors
group_colors = {
    'Languajes': '#003f5c',
    'Utilities': '#2f4b7c',
    'Databases': '#665191',
    'Microservices': '#a05195',
    'GitOps': '#d45087',
    'DevOps': '#f95d6a',
    'Observability': '#ff7c43',
    'Cloud': '#ffa600'
}

# Sorting and grouping technologies by categories and years of experience
sorted_grouped_tech = {}
for tech, years in tech_experience.items():
    group = groups[tech]
    if group not in sorted_grouped_tech:
        sorted_grouped_tech[group] = []
    sorted_grouped_tech[group].append((tech, years))

# Flattening the sorted and grouped technologies for plotting
technologies = []
years_of_experience = []
colors = []

for group, techs in sorted_grouped_tech.items():
    techs.sort(key=lambda x: x[1], reverse=True)  # Sort technologies within each group
    for tech, years in techs:
        technologies.append(tech)
        years_of_experience.append(years)
        colors.append(group_colors[group])

# Creating the bar graph
y_pos = np.arange(len(technologies))

plt.figure(figsize=(11, 6))
bars = plt.barh(y_pos, years_of_experience, align='center', color=colors, alpha=0.7)
ax = plt.gca()
ax.invert_yaxis()  # Invert y-axis to display the most experience at the top
plt.yticks(y_pos, technologies)
plt.xlabel('Years')
# plt.title('Experience by Technology')

# Set spine and tick line colors
spine_color = '#bbbbbb'  # Change this to your desired color
plt.setp(ax.spines.values(), color=spine_color)
plt.setp([ax.get_xticklines(), ax.get_yticklines()], color=spine_color)

# Create a legend for the groups
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=group) for group, color in group_colors.items()]
plt.legend(handles=legend_elements, title='Area', facecolor='white', framealpha=1, edgecolor='white', borderpad=0)

plt.tight_layout(pad=0)
plt.show()

# Save the plot with zero margins
plt.savefig(output_file, bbox_inches='tight', pad_inches=0.02, format='png')
