# PERF_VARIABLE = {
#   "locust_config": {
#     "swarm": 10.0,
#     "spawn": 100.0
#   },
#   "users": {
#     "websiteuser": {
#       "type": "httpuser",
#       "wait_time": "between(5,10)",
#       "host": "https://google.com",
#       "tasks": [
#         {
#           "action": "post",
#           "data": "/submit/form",
#           "name": "visit_homepage"
#         },
#         {
#           "action": "get",
#           "data": "/submit/form",
#           "name": "just_homepage"
#         }
#       ]
#     },
#     "anotheruser": {
#       "type": "user",
#       "wait_time": "between(5,10)",
#       "host": "https://twitter.com",
#       "tasks": []
#     }
#   }
# }

PERF_VARIABLE = {
  "locust_config": {
    "swarm": "10",
    "spawn": "100"
  },
  "task_sets": [
    {
      "task_set_name": "TaskSet1",
      "sequential": True,
      "tasks": [
        {
          "action": "get",
          "data": "/submit/form",
          "name": "WebsiteUser"
        },
        {
          "action": "get",
          "data": "/submit/form",
          "name": "WebsiteUser"
        }

      ]
    },
    {
      "task_set_name": "TaskSet2",
      "sequential": False,
      "tasks": [
        {
          "action": "get",
          "data": "/submit/form",
          "name": "WebsiteUser"
        },
        {
          "action": "get",
          "data": "/submit/form",
          "name": "WebsiteUser"
        }

      ]
    }
  ],
  "users": {
    "WebsiteUser": {
      "type": "HttpUser",
      "wait_time": "between(5,10)",
      "host": "https://google.com",
      "task_sets": ["TaskSet1", "TaskSet2"],
      "tasks": []
    },
    "AnotherUser": {
      "type": "USER",
      "wait_time": "between(5,10)",
      "host": "https://twitter.com",
      "task_sets": ["TaskSet1"],
      "tasks": [
        {
          "action": "get",
          "data": "/submit/form",
          "name": "WebsiteUser"
        }
      ]
    }
  }
}

# for key in PERF_VARIABLE['users']:
#   print(key)

# for task in PERF_VARIABLE['users']['websiteuser']['tasks']:
#   print(task)

from jinja2 import Environment, FileSystemLoader

# Load template file
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template("py_perf_temp.txt")
output = template.render(PERF_VARIABLE=PERF_VARIABLE)
print(output)
