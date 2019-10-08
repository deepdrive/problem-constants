from datetime import datetime

import os

###############################################################
# WARNING: These are shared with                              #
# https://github.com/deepdrive/problem-coordinator/constants.py #
###############################################################

GCP_REGION = 'us-west1'
GCP_ZONE = GCP_REGION + '-b'
GCP_PROJECT = os.environ.get('GOOGLE_CLOUD_PROJECT') or \
              os.environ.get('GCP_PROJECT') or 'silken-impulse-217423'

WORKER_INSTANCE_LABEL = 'deepdrive-worker'
WORKER_INSTANCES_COLLECTION_NAME = 'deepdrive_worker_instances'
JOBS_COLLECTION_NAME = 'deepdrive_jobs'
EVAL_CONFIG_COLLECTION_NAME = 'deepdrive_eval_config'
JOB_LOOP_ID = 'deepdrive_job_loop'

CONTAINER_RUN_OPTIONS = dict(runtime='nvidia', network='host')

# Eventually needs to be divisible by 2 as we start a problem and bot
# instance for each eval. Now they're on the same instance.
MAX_WORKER_INSTANCES = 3
MAX_EVAL_SECONDS_DEFAULT = 5 * 60

# This should be public for submitters to see logs
BOTLEAGUE_LOG_BUCKET = 'deepdriveio'

BOTLEAGUE_LOG_DIR = 'deepdrive_botleague_logs'
BOTLEAGUE_RESULTS_DIR = '/mnt/botleague_results'
BOTLEAGUE_INNER_RESULTS_DIR_NAME = 'latest'
BOTLEAGUE_RESULTS_FILEPATH = f'{BOTLEAGUE_RESULTS_DIR}/results.json'
BOTLEAGUE_LIAISON_HOST = os.environ.get('BOTLEAGUE_LIAISON_HOST',
                                        default='https://liaison.botleague.io')

JOB_TYPE_EVAL = 'eval'
JOB_TYPE_SIM_BUILD = 'sim-build'
JOB_TYPE_DEEPDRIVE_BUILD = 'deepdrive-build'

JOB_STATUS_CREATED = 'created'
JOB_STATUS_ASSIGNED = 'assigned'
JOB_STATUS_RUNNING = 'running'
JOB_STATUS_FINISHED = 'finished'
JOB_STATUS_TIMED_OUT = 'timed_out'
JOB_STATUS_DENIED_CONFIRMATION = 'denied_confirmation'
JOB_STATUS_UNSUPPORTED_PROBLEM = 'unsupported_problem'

INSTANCE_STATUS_AVAILABLE = 'available'
INSTANCE_STATUS_USED = 'used'
INSTANCE_CONFIG_PATH = 'cloud_configs/worker_instance_create.json'
INSTANCE_NAME_PREFIX = 'deepdrive-worker-'

METADATA_URL = 'http://metadata.google.internal/computeMetadata/v1/instance'

HOST = os.environ.get('PROBLEM_ENDPOINT_HOST',
                      default='https://sim.deepdrive.io')
SUPPORTED_PROBLEMS = ['domain_randomization']

DIR_DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
DATE_STR = datetime.utcnow().strftime(DIR_DATE_FORMAT)
LOCAL_INSTANCE_ID = 'asdf'
