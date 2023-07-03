{{/*
Expand the name of the chart.
*/}}
{{- define "node-red.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "node-red.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "node-red.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "node-red.labels" -}}
helm.sh/chart: {{ include "node-red.chart" . }}
{{ include "node-red.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "node-red.selectorLabels" -}}
app.kubernetes.io/name: {{ include "node-red.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "node-red.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "node-red.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}

{{/*
Create the name of the configmap
*/}}
{{- define "node-red.configMapName" -}}
{{ printf "%s-npmrc-cm" (include "node-red.fullname" $) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create the name of the sidecar-configmap
*/}}
{{- define "node-red.sidecarConfigMapName" -}}
{{ printf "%s-flow-refresh-cm" (include "node-red.fullname" $) | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create the name of the certificate
*/}}
{{- define "node-red.certificateName" -}}
{{ printf "%s-cert" (include "node-red.fullname" $) | trunc 63 | trimSuffix "-" }}
{{- end }}


