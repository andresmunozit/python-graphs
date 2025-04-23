import matplotlib.pyplot as plt
import numpy as np

# Set the global font to be 'Arial', size 10
plt.rcParams['font.family'] = 'monospace'
plt.rcParams['font.size'] = 11

output_file = '/output/plot.png'

# Defining the technologies and corresponding years of experience
tech_experience = {
    'JavaScript': 6,
    'Java': 2,
    'Golang': 1,
    'Ruby': 2,
    'Python': 1,
    'TypeScript': 4,
    'Bash': 3,
    'Node.js': 6,
    'Express': 5,
    'NestJS': 2,
    'GraphQL': 2,
    'MongoDB': 3,
    'PostgreSQL': 3,
    'Redis': 2,
    'GRPC': 1,
    'Kafka': 3,
    'RabbitMQ': 3,
    'Git': 5,
    'Docker': 3,
    'Kubernetes': 3,
    'DataDog': 2,
    'Prometheus': 2,
    'Grafana': 1,
    'AWS': 3,
    'Google Cloud': 2,
    'Azure': 1,
}
# Grouping related technologies and defining colors
group_colors = {
    'Languajes': '#845EC2',
    'API Development': '#2C73D2',
    'Databases': '#FF6F91',
    'Microservices': '#0089BA',
    'DevOps': '#FF9671',
    'Observability': '#008F7A',
    'Cloud': '#0081CF'
}

groups = {
    'Java': 'Languajes',
    'JavaScript': 'Languajes',
    'Golang': 'Languajes',
    'Ruby': 'Languajes',
    'Python': 'Languajes',
    'TypeScript': 'Languajes',
    'Bash': 'Languajes',
    'Node.js': 'API Development', 
    'Express': 'API Development',
    'NestJS': 'API Development',
    'GraphQL': 'API Development',
    'MongoDB': 'Databases', 
    'PostgreSQL': 'Databases',
    'Redis': 'Databases',
    'GRPC': 'Microservices', 
    'Kafka': 'Microservices',
    'RabbitMQ': 'Microservices',
    'Git': 'DevOps',
    'Docker': 'DevOps', 
    'Kubernetes': 'DevOps',
    'DataDog': 'Observability',
    'Prometheus': 'Observability',
    'Grafana': 'Observability',
    'AWS': 'Cloud',
    'Google Cloud': 'Cloud',
    'Azure': 'Cloud',
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

plt.figure(figsize=(12, 6))
bars = plt.barh(y_pos, years_of_experience, align='center', color=colors, alpha=0.7)
plt.gca().invert_yaxis()  # Invert y-axis to display the most experience at the top
plt.yticks(y_pos, technologies)
plt.xlabel('Years')
plt.title('Experience by Technology')

# Create a legend for the groups
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=group) for group, color in group_colors.items()]
plt.legend(handles=legend_elements, title='Area')

plt.tight_layout()
plt.show()

# Save the plot instead of showing it
plt.savefig(output_file)
