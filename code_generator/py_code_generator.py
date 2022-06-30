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

# PERF_VARIABLE = {
#   "locust_config": {
#     "swarm": "10",
#     "spawn": "100"
#   },
#   "task_sets": [
#     {
#       "task_set_name": "TaskSet1",
#       "sequential": True,
#       "tasks": [
#         {
#           "action": "get",
#           "data": "/submit/form",
#           "name": "WebsiteUser"
#         },
#         {
#           "action": "get",
#           "data": "/submit/form",
#           "name": "WebsiteUser"
#         }
#
#       ]
#     },
#     {
#       "task_set_name": "TaskSet2",
#       "sequential": False,
#       "tasks": [
#         {
#           "action": "get",
#           "data": "/submit/form",
#           "name": "WebsiteUser"
#         },
#         {
#           "action": "get",
#           "data": "/submit/form",
#           "name": "WebsiteUser"
#         }
#
#       ]
#     }
#   ],
#   "users": {
#     "WebsiteUser": {
#       "type": "HttpUser",
#       "wait_time": "between(5,10)",
#       "host": "https://google.com",
#       "task_sets": ["TaskSet1", "TaskSet2"],
#       "tasks": []
#     },
#     "AnotherUser": {
#       "type": "USER",
#       "wait_time": "between(5,10)",
#       "host": "https://twitter.com",
#       "task_sets": ["TaskSet1"],
#       "tasks": [
#         {
#           "action": "get",
#           "data": "/submit/form",
#           "name": "WebsiteUser"
#         }
#       ]
#     }
#   }
# }

# for key in PERF_VARIABLE['users']:
#   print(key)

# for task in PERF_VARIABLE['users']['websiteuser']['tasks']:
#   print(task)

# PERF_VARIABLE = {
#   "locust_config": {
#     "swarm": 10.0,
#     "spawn": 100.0
#   },
#   "users": {
#     "User1": {
#       "type": "HttpUser",
#       "wait_time": "between(5,10)",
#       "host": "https://google.com",
#       "tasks": [
#         {
#           "action": "post",
#           "data": "/hello1",
#           "name": "visit_homepage"
#         },
#         {
#           "action": "post",
#           "data": "/hello2",
#           "name": "visit_indexpage"
#         }
#       ]
#     },
#     "User2": {
#       "type": "User",
#       "wait_time": "between(5,10)",
#       "host": "https://twitter.com",
#       "tasks": [
#         {
#           "action": "post",
#           "data": "/hello2",
#           "name": "visit_indexpage"
#         }
#       ]
#     },
#     "User3": {
#       "type": "User",
#       "wait_time": "between(5,10)",
#       "host": "https://twitter.com",
#       "tasks": []
#     }
#   }
# }

# PERF_VARIABLE = {
#   "locust_config": {
#     "swarm": 10.0,
#     "spawn": 100.0
#   },
#   "users": {
#     "User1": {
#       "type": "HttpUser",
#       "wait_time": "between(5,10)",
#       "host": "https://http.cat",
#       "tasks": [
#         {
#           "action": "get",
#           "data": "/100",
#           "name": "visit_homepage"
#         },
#         {
#           "action": "get",
#           "data": "/300",
#           "name": "visit_indexpage"
#         }
#       ]
#     },
#     "User2": {
#       "type": "User",
#       "wait_time": "between(5,10)",
#       "host": "https://http.cat",
#       "tasks": [
#         {
#           "action": "get",
#           "data": "/400",
#           "name": "visit_indexpage"
#         }
#       ]
#     },
#     "User3": {
#       "type": "User",
#       "wait_time": "between(5,10)",
#       "host": "https://http.cat",
#       "tasks": []
#     }
#   }
# }

PERF_VARIABLE = {
  "locust_config": {
    "swarm": 10.0,
    "spawn": 100.0
  },
  "users": {
    "User1": {
      "type": "HttpUser",
      "wait_time": "between(5,10)",
      "host": "https://http.cat",
      "tasks": [
        {
          "action": "get",
          "data": "/100",
          "name": "visit_homepage"
        },
        {
          "action": "get",
          "data": "/300",
          "name": "visit_indexpage"
        }
      ]
    },
    "User2": {
      "type": "HttpUser",
      "wait_time": "between(5,10)",
      "host": "https://http.cat",
      "tasks": [
        {
          "action": "get",
          "data": "/400",
          "name": "visit_indexpage"
        }
      ]
    },
    "User3": {
      "type": "User",
      "wait_time": "between(5,10)",
      "host": "https://http.cat",
      "tasks": []
    }
  }
}

import subprocess
import os
from jinja2 import Environment, FileSystemLoader


def load_jinja_template_and_generate_locust_py(jinja_template_dir="", jinja_file_path="",
                                               jinja2_template_variable=None, output_file_path=""):
    file_loader = FileSystemLoader(jinja_template_dir)
    env = Environment(loader=file_loader)
    template = env.get_template(jinja_file_path)
    output = template.render(PERF_VARIABLE=jinja2_template_variable)
    print(output)

    # output_file = open("output_python_file.py", "w")
    # output_file.write(output)
    # output_file.close()

    with open(output_file_path, "w") as output_file:
        output_file.write(output)


if __name__ == "__main__":
    jinja2_temp_dir = os.path.dirname(os.path.realpath(__file__)) + os.sep + "templates"
    output_py_file = f"{os.path.dirname(os.path.realpath(__file__))}{os.sep}locust_file{os.sep}output_python_file_5.py"
    load_jinja_template_and_generate_locust_py(jinja_template_dir=jinja2_temp_dir,
                                               jinja_file_path="py_perf_temp.txt",
                                               jinja2_template_variable=PERF_VARIABLE,
                                               output_file_path=output_py_file)
    # subprocess.run("echo hello world", shell=True)
    # subprocess.run("dir", shell=True)
    command = ["locust", "-f", output_py_file]
    # sp = subprocess.run(command, shell=False, capture_output=True)
    # print(sp.stdout)
    sp = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # rtrn = sp.wait()
    print(sp.pid)
    out, err = sp.communicate()
    print(out)
