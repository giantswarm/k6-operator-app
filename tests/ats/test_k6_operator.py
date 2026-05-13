import logging
from typing import List, Tuple

import pytest
import pykube
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.k8s.deployment import wait_for_deployments_to_run


logger = logging.getLogger(__name__)

namespace_name = "k6-operator"
deployment_name = "k6-operator-k6operator-controller-manager"

timeout: int = 900

@pytest.mark.smoke
def test_api_working(kube_cluster: Cluster) -> None:
    """Very minimalistic example of using the [kube_cluster](pytest_helm_charts.fixtures.kube_cluster)
    fixture to get an instance of [Cluster](pytest_helm_charts.clusters.Cluster) under test
    and access its [kube_client](pytest_helm_charts.clusters.Cluster.kube_client) property
    to get access to Kubernetes API of cluster under test.
    Please refer to [pykube](https://pykube.readthedocs.io/en/latest/api/pykube.html) to get docs
    for [HTTPClient](https://pykube.readthedocs.io/en/latest/api/pykube.html#pykube.http.HTTPClient).
    """
    assert kube_cluster.kube_client is not None
    assert len(pykube.Node.objects(kube_cluster.kube_client)) >= 1

# scope "module" means this is run only once, for the first test case requesting! It might be tricky
# if you want to assert this multiple times
# -- Checking that k6-operator's deployment is present on the cluster
@pytest.fixture(scope="module")
def deployment(kube_cluster: Cluster) -> pykube.Deployment:
    logger.info("Waiting for k6-operator deployment to be deployed..")

    deployment_ready = wait_for_deployments_to_run(
        kube_cluster.kube_client,
        [deployment_name],
        namespace_name,
        timeout,
    )

    logger.info("k6-operator deployment is deployed..")
    return deployment_ready

@pytest.fixture(scope="module")
def pods(kube_cluster: Cluster) -> pykube.Pod:
    pods = pykube.Pod.objects(kube_cluster.kube_client)

    pods = pods.filter(namespace=namespace_name, selector={
                       'app.kubernetes.io/name': 'k6-operator', 'app.kubernetes.io/instance': 'k6-operator'})

    return pods

# when we start the tests on circleci, we have to wait for pods to be available, hence
# this additional delay and retries
# -- Checking that all pods from k6-operator's deployment is available (i.e in "Ready" state)
@pytest.mark.smoke
@pytest.mark.upgrade
@pytest.mark.flaky(reruns=5, reruns_delay=10)
def test_pods_available(deployment: pykube.Deployment):
    assert int(deployment.obj["status"]["readyReplicas"]) == int(deployment.obj["spec"]["replicas"])
