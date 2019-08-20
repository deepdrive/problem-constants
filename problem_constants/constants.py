import os

###############################################################
# WARNING: These are shared with                              #
# https://github.com/deepdrive/problem-coordinator/constants.py #
###############################################################

GCP_REGION = 'us-west1'
GCP_ZONE = GCP_REGION + '-b'
GCP_PROJECT = os.environ.get('GOOGLE_CLOUD_PROJECT') or \
              os.environ.get('GCP_PROJECT') or 'silken-impulse-217423'

STACKDRIVER_LOG_NAME = 'deepdrive-problem-endpoint'
INSTANCE_EVAL_LABEL = 'deepdrive-eval'
EVAL_INSTANCES_COLLECTION_NAME = 'deepdrive_eval_instances'
EVAL_JOBS_COLLECTION_NAME = 'deepdrive_eval_jobs'
EVAL_CONFIG_COLLECTION_NAME = 'deepdrive_eval_config'
EVAL_LOOP_ID = 'deepdrive_eval_loop'

CONTAINER_RUN_OPTIONS = dict(runtime='nvidia', network='host')

# Needs to be divisible by 2 as we start a problem and bot instance for each
# eval
MAX_EVAL_INSTANCES = 6
MAX_EVAL_SECONDS_DEFAULT = 5 * 60

# This should be public for submitters to see logs
BOTLEAGUE_LOG_BUCKET = 'deepdriveio'

BOTLEAGUE_LOG_DIR = 'botleague_eval_logs'
BOTLEAGUE_RESULTS_DIR = '/mnt/botleague_results'
BOTLEAGUE_INNER_RESULTS_DIR_NAME = 'latest'
BOTLEAGUE_RESULTS_FILEPATH = f'{BOTLEAGUE_RESULTS_DIR}/results.json'
BOTLEAGUE_LIAISON_HOST = os.environ.get('BOTLEAGUE_LIAISON_HOST',
                                        default='https://liaison.botleague.io')

JOB_STATUS_CREATED = 'created'
JOB_STATUS_CONFIRMED = 'confirmed'
JOB_STATUS_ASSIGNED = 'assigned'
JOB_STATUS_RUNNING = 'running'
JOB_STATUS_FINISHED = 'finished'
JOB_STATUS_TIMED_OUT = 'timed_out'
JOB_STATUS_DENIED_CONFIRMATION = 'denied_confirmation'
JOB_STATUS_UNSUPPORTED_PROBLEM = 'unsupported_problem'

INSTANCE_STATUS_AVAILABLE = 'available'
INSTANCE_STATUS_USED = 'used'
INSTANCE_CONFIG_PATH = 'cloud_configs/eval_instance_create.json'
INSTANCE_NAME_PREFIX = 'deepdrive-eval-problem-worker-'

METADATA_URL = 'http://metadata.google.internal/computeMetadata/v1/instance'

HOST = os.environ.get('PROBLEM_ENDPOINT_HOST',
                      default='https://sim.deepdrive.io')
RESULTS_CALLBACK = f'{BOTLEAGUE_LIAISON_HOST}/results'
SUPPORTED_PROBLEMS = ['domain_randomization']
ROOT = os.path.dirname(os.path.realpath(__file__))
